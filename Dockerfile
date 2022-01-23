# syntax=docker/dockerfile:1
FROM thinkwhere/gdal-python
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt


