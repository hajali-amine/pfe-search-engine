FROM node:12-alpine as builder
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
ENV REACT_APP_BACKEND_URL=http://localhost:5000
RUN npm run build

FROM nginx:1.19.0
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/build .
EXPOSE 80
ENTRYPOINT [ "nginx", "-g", "daemon off;" ]
