# MAINTAINER        ZhangPeng <zhangpeng18@hotmail.com>
# DOCKER-VERSION    19.03.2, build 6a30dfc

FROM python:3.6.9-alpine3.10
LABEL maintainer="zhangpeng18@hotmail.com"

RUN mkdir -p /usr/src/app  && \
    mkdir -p /var/log/gunicorn

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir gunicorn && \
    pip install --no-cache-dir -r /usr/src/app/requirements.txt && \
    pip install --ignore-installed six

COPY . /usr/src/app

EXPOSE 8000

CMD ["/usr/local/bin/gunicorn", "-w", "4", "-b", ":8000", "wsgi:app"]