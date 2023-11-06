FROM python:3.11-slim-bullseye
WORKDIR /app
COPY requirements.txt /app/
RUN mkdir /app/media
RUN mkdir /app/static
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/
