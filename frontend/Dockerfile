FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY public/ /usr/share/nginx/html/

RUN chmod -R 755 /usr/share/nginx/html/

EXPOSE 80

# Nginx automatically serves index.html as the entry point
CMD ["nginx", "-g", "daemon off;"]
