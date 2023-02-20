FROM python:3.9

RUN pip install pipenv
RUN apt-get -q update && apt-get install -y --no-install-recommends gcc supervisor && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

RUN mkdir artefacts

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy --ignore-pipfile


COPY pipelines ./pipelines
COPY common ./common

COPY main.py ./main.py

CMD ["python", "-m", "main"]