FROM alpine 
RUN apk add --update nodejs-npm
RUN apk add --update git
RUN apk add --update nano

RUN git clone https://github.com/ghulamMustafaRaza/learn-docker /app

WORKDIR /app/docker-hello-world

RUN npm install

CMD npm start