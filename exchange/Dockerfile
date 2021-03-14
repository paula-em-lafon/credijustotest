
# pull official base image
FROM python:alpine

# set work directory
WORKDIR /usr/src/exchange

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev\
     musl-dev jpeg-dev zlib-dev libxml2-dev libxslt-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .