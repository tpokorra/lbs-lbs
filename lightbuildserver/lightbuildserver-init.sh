#!/bin/bash

chown -R uwsgi:uwsgi /usr/share/lightbuildserver/
chown uwsgi:uwsgi /etc/uwsgi.d/lightbuildserver.ini
chown uwsgi:uwsgi /var/log/uwsgi.log
usermod -a nginx -G uwsgi
touch /var/log/uwsgi.log
chown uwsgi:uwsgi /var/log/uwsgi.log
