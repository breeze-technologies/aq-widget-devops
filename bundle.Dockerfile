FROM node:12.10.0-alpine

LABEL version="1.0.0"
LABEL description="AQ Widget bundle including API backend and widget frontend."

WORKDIR /usr/src/app

COPY ./aq-widget-api ./aq-widget
COPY ./aq-widget-app/dist ./aq-widget/dist/public/
COPY ./aq-client-eea ./aq-widget/node_modules/aq-client-eea

RUN mkdir /usr/src/app/datastore && \
    mkdir /usr/src/app/logs

ENV STORAGE_DIR=/usr/src/app/datastore
ENV LOG_DIR=/usr/src/app/logs
VOLUME /usr/src/app/datastore /usr/src/app/logs

WORKDIR /usr/src/app/aq-widget

ENTRYPOINT node dist/index.js