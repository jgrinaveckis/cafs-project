FROM node:19.9.0-alpine
RUN apk add --no-cache --virtual .gyp \
        python \
        make \
        g++ \
    && npm install \
    && apk del .gyp
WORKDIR /var/www/
ENTRYPOINT ["npm", "install"]