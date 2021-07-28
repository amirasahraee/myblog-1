FROM python:3.9-alpine

WORKDIR /pland-back
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev bash
RUN apk --no-cache add python3-dev build-base linux-headers pcre-dev
#                       # Pillow dependencies
#                       jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev \
#                       tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev
RUN python3.9 -m pip install virtualenv && pip install --upgrade pip

