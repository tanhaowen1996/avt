## 该项目为视频转码接口，只有一个post请求接口
### 请求方式为
```curl -X POST -F "file=@input.mp4" http://url:port/videos/ --output output.mp4```

### 操作步骤制作Docker镜像：
docker build -t . {name}:{tag}

### 运行参数:
#### 容器内部默认端口是18006，可以使用 -e WEB_PORT={port}来修改容器内部端口
```docker run -itd --name test-avt1 -p 9000:18006 -e SERVICE_MODE="asgi" avt:v1.0```
