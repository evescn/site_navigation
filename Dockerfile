# 使用轻量级的 Alpine Linux 作为最终容器
FROM alpine:3.16.0

WORKDIR /app

# 设置时区
RUN apk add --no-cache tzdata \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV TZ=Asia/Shanghai

# 定义环境变量 GIN_MODE=release
ENV GIN_MODE=release

# 复制构建环境中的二进制文件到最终容器中
COPY app .
COPY config config
# 定义启动命令，将输出重定向到日志文件
CMD ["/bin/sh", "-c", "./app >> /app/log/stout.log 2>&1"]