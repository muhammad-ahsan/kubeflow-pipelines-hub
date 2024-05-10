FROM python:3.9-slim

RUN pip install --upgrade pip setuptools
RUN apt-get update \
    && apt-get install -y gcc python3-dev

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]