FROM python:3.12.5-alpine3.20
RUN mkdir /fast-app
COPY . /fast-app/
RUN pip3  install --no-cache-dir --upgrade -r /fast-app/requirements.txt
WORKDIR /fast-app