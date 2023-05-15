FROM nikolaik/python-nodejs:python3.10-nodejs19-slim

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    python3-gdal \
    libgeos-dev \
    gettext

COPY requirements.txt /app/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/okp/:/app/backend/"

# RUN apt-get update && apt-get install -y gettext

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

# WORKDIR /app/frontend/
# RUN npm install
# RUN npm run build
# EXPOSE 3000

WORKDIR /app