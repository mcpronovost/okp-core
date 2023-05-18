FROM node:20.1.0

# for caching optimisations
COPY package*.json /
RUN npm install

COPY . /app
WORKDIR /app

ENV PATH=/node_modules/.bin:$PATH
