FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Geogramint/requirements.txt /tmp/requirements.txt

RUN apt-get update && apt-get install libfreetype6-dev

RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

COPY Geogramint /app

WORKDIR /app

EXPOSE 8000

RUN adduser --disabled-password app-user

USER app-user

ENTRYPOINT ["python", "geogramint.py"]