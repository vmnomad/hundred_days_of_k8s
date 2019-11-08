#!/bin/sh
cd /hundred_days_of_k8s

#prepare nging config
cp website.conf /etc/nginx/conf.d/
cp proxy_params /etc/nginx/
cp certificates/domain-crt.crt /etc/nginx/
cp certificates/domain-key.key /etc/nginx/
rm /etc/nginx/conf.d/default.conf
mkdir -p /run/nginx

# start gunicorn as Daemon
gunicorn --access-logfile - --workers 3 -D --bind unix:/hundred_days_of_k8s/myproject.sock hundred_days_of_k8s.wsgi:application

# start nginx
/usr/sbin/nginx -c /etc/nginx/nginx.conf

while true; do
    sleep 60
done