FROM python:3.8-alpine
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add postgresql-dev gcc python3-dev musl-dev
