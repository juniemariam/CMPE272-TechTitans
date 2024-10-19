### Stage 1: build ###

FROM node:18-alpine as builder

# Set working directory.
RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
COPY angular-app/package.json angular-app/package-lock.json /app/angular-app/

# Install app dependencies.
RUN npm install --prefix angular-app

# Copy app files.
COPY . /app

# Build app
RUN npm run build --prefix angular-app -- --output-path=./dist/out


### Stage 2: delivery ###

FROM nginx:alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy output directory from builder to nginx image.
COPY --from=builder /app/angular-app/dist/out/browser /usr/share/nginx/html

# Ensure correct permissions
RUN chmod -R 755 /usr/share/nginx/html

# Copy nginx configuration file.
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80