FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies needed for some Python packages like mysqlclient and psycopg
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip pipenv

COPY Pipfile Pipfile.lock /app/

# Install dependencies directly into the system running in the container
RUN pipenv install --system --deploy --ignore-pipfile || pipenv install --system --skip-lock

COPY . /app/

