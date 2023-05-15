FROM node:lts AS build

WORKDIR /app/frontend

COPY ./package.json ./
COPY ./package-lock.json ./

RUN npm install --silent

COPY . .

RUN npm run build -- --mode custom

COPY . .

ENV HOST=0.0.0.0
ENV PORT=3000
