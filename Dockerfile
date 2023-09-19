FROM python:3.10-slim

RUN pip install fastapi uvicorn wheel virtualenv

EXPOSE 8001

WORKDIR /usr/src/api
COPY . /api/src
COPY ./main.py /api
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./