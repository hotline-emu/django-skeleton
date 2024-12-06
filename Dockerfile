FROM python:3.10-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry \
    && poetry install
