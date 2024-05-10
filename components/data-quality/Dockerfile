FROM python:3.9-slim

WORKDIR app

COPY data-contract ./data-contract
COPY dataset ./dataset

COPY main.py .
COPY data_quality.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt