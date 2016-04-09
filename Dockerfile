FROM python:2.7

ENV_FILE:
    - ./common.env
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
