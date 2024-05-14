FROM python:3.9-slim

RUN pip install --upgrade pip setuptools
RUN apt-get update \
    && apt-get install -y gcc python3-dev

# Install pipenv
RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

# Install dependencies using pipenv
RUN pipenv install --deploy --system

COPY . .

CMD ["python", "main.py"]