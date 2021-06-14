FROM python:3.7-alpine3.9

RUN apk update && apk add bash build-base python3-dev libffi-dev

ADD client.py /client/

WORKDIR /client/

