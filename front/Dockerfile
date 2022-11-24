# Build Frontend
FROM node:12-alpine AS builder
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
ENV REACT_APP_BACKEND_URL=http://localhost:5000
RUN npm run build

# Serve Front with Nginx
FROM nginx:1.19.0
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/build .
EXPOSE 80
ENTRYPOINT [ "nginx", "-g", "daemon off;" ]
