# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.10.4-alpine3.14
LABEL maintainer="andriyvvoznyuk@gmail.com"

ENV DockerHOME=/usr/src/app
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PORT=8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install "gunicorn==20.0.4"
# Install system packages required by Wagtail and Django.
# Install server packages
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev \
    && apk add jpeg-dev libwebp-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxml2-dev libxslt-dev libxml2


# Install python packages
RUN pip install --upgrade pip
RUN pip install "gunicorn==20.0.4"
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt




