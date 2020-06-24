FROM python:3.8-slim as builder

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt > requirements.txt


FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/stock

COPY --from=builder /app/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . .

EXPOSE 80
CMD [ "gunicorn", "-w", "4", "-b", ":80", "-k", "uvicorn.workers.UvicornWorker","main:app" ]