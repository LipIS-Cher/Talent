# base image
FROM node:12-buster-slim

# set working directory
WORKDIR /react_app

# add `/react_app/node_modules/.bin` to $PATH
ENV PATH /react_app/node_modules/.bin:$PATH

# install and cache react_app dependencies
COPY package.json /react_app/package.json
RUN npm install

# start react_app
CMD ["npm", "start"]