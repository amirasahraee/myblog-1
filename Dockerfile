FROM python:3.9-alpine

WORKDIR /myblog-back
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev bash
RUN apk  add python3-dev build-base linux-headers pcre-dev jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev \
tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev
RUN python3.9 -m pip install virtualenv && pip install --upgrade pip
