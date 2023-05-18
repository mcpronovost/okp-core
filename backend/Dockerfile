FROM python:3.11.3

RUN apt-get clean && apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gettext

COPY requirements.txt /app/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/okp/:/app/apps/"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/