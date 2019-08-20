#!/usr/bin/env bash
# Set up web servers for deployment

if ! which nginx > /dev/null 2>&1; then
    apt-get update
    apt-get -y install nginx
    ufw allow 'Nginx HTTP'
fi

if [ ! -d /data/ ]; then
	mkdir /data/
fi
if [ ! -d /data/web_static ]; then
	mkdir /data/web_static/
fi
if [ ! -d /data/web_static/releases/ ]; then
	mkdir /data/web_static/releases/
fi
if [ ! -d /data/web_static/shared/ ]; then
	mkdir /data/web_static/shared/
fi
if [ ! -d /data/web_static/releases/test/ ]; then
	mkdir /data/web_static/releases/test/
fi
printf "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>\n" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}" /etc/nginx/sites-available/default
service nginx restart
