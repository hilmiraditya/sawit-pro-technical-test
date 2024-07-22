FROM --platform=linux/amd64 ubuntu:jammy

WORKDIR /app

ENV TZ=Asia/Jakarta

RUN apt-get update \
    && apt-get install -y wget \
    && apt-get install -y unzip \
    && apt-get install -y python3 \
    && apt-get install -y supervisor

RUN mkdir -p /var/log \
    && wget https://github.com/grafana/loki/releases/download/v2.2.1/promtail-linux-amd64.zip \
    && unzip promtail-linux-amd64.zip \
    && mv promtail-linux-amd64 /usr/local/bin/promtail \
    && rm promtail-linux-amd64.zip

COPY ./promtail-config.yaml /etc/promtail/promtail-config.yaml
COPY ./log-generator.py /app/log-generator.py
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 9080