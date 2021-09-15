# usage: docker build -t avt:IMAGE_VERSION .
FROM registry-itwork.yonghui.cn/library/python:3.9-slim
MAINTAINER YH
ENV LANG en_US.UTF-8
RUN sed -i -e 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN apt update && apt install vim ffmpeg libmagic1 -y

ENV TZ Asia/Shanghai
RUN ln -s -f /usr/share/zoneinfo/$TZ /etc/localtime
RUN echo $TZ > /etc/timezone
RUN mkdir -p /opt/tmp/
ENV opt /opt
WORKDIR ${opt}
ADD . .
RUN pip3 install -U -i https://mirrors.aliyun.com/pypi/simple/ pip
RUN pip3 install -U -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
RUN python3 manage.py collectstatic --no-input
CMD ["/bin/sh", "runserver.sh"]