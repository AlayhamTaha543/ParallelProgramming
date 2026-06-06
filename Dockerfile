FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# copy dependency files first for better caching
COPY Pipfile Pipfile.lock /app/

# install pipenv and system dependencies
RUN pip install --upgrade pip pipenv && \
    pipenv install --system --deploy || pipenv install --system

# copy application code
COPY . /app

ENV PORT=8001

RUN mkdir -p /vol/static

EXPOSE 8000

CMD ["bash", "/app/scripts/gunicorn_start.sh"]
