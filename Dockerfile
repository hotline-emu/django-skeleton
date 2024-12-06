FROM python:3.10-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && poetry install --no-dev

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
