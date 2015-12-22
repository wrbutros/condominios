FROM python:2.7

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE condominios.settings.sqlite

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
