FROM ubuntu:18.04

LABEL maintainer="Pratik Saha <saha.pratik04@gmail.com>"

RUN apt-get update && \
    apt-get install -y python3 python3-dev python3-pip curl

COPY ./requirements.txt /code/requirements.txt

WORKDIR /code

RUN pip3 install -r requirements.txt

COPY . /code

RUN python3 setup.py develop
