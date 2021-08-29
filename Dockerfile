# syntax=docker/dockerfile:1
FROM thinkwhere/gdal-python
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

