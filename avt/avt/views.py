from django.http import HttpResponse
from django.views import View
from rest_framework import status
import uuid
import magic
import os


class Avt(View):
    def post(self, request):
        if request.FILES.get('file'):
            filename = request.FILES.get('file').name.split(".")[0]
            filename = str(uuid.uuid4()) + filename
            file = request.FILES.get('file')
            with open("/opt/tmp/{0}.mp4".format(filename), 'wb+') as save_file:
                for chunk in file.chunks():
                    save_file.write(chunk)
            if file.size > 52428800:
                return HttpResponse('file size {0}MB is too large, maximum limit 50MB'
                                    .format(file.size/1024/1024), status=status.HTTP_400_BAD_REQUEST)

            mtype = magic.from_file("/opt/tmp/{0}.mp4".format(filename), mime=True)
            if not mtype.startswith('video'):
                return HttpResponse('invalid mime type:{0}, accept videos/mp4'
                                    .format(mtype), status=status.HTTP_400_BAD_REQUEST)

            cmd = 'ffmpeg -i ' + '/opt/tmp/{0}.mp4'.format(filename) \
                  + ' -vcodec libx264 -vf ' \
                    '\"fps=12,scale=1280:trunc(ow/a/2)*2\" ' \
                    '-acodec aac -profile:a aac_low ' \
                    '-profile:v high -maxrate 2000k ' \
                    '-movflags faststart ' + '/opt/tmp/{0}_out.mp4 \
                                    -y'.format(filename)
            os.system(cmd)
            re_avt = open("/opt/tmp/{0}_out.mp4".format(filename), 'rb').read()
            os.system("rm -f /opt/tmp/{0}.mp4 /opt/tmp/{0}_out.mp4".format(filename))
            return HttpResponse(re_avt, content_type='video/mp4')
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
