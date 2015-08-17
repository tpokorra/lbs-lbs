#!/bin/bash

chown -R uwsgi:uwsgi /usr/share/lightbuildserver/
chown uwsgi:uwsgi /etc/uwsgi.d/lightbuildserver.ini
usermod -a nginx -G uwsgi
touch /var/log/uwsgi.log
chown uwsgi:uwsgi /var/log/uwsgi.log

etccontainerpath=/etc/lightbuildserver/container
echo "this key will be used to login to the host for the containers."
echo "leave the passwort empty!"
mkdir -p $etcpath
ssh-keygen -t rsa -f $etccontainerpath/container_rsa
chown -R uwsgi:uwsgi $etccontainerpath

# for using the local machine as a host for the containers
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh/authorized_keys
cat $etccontainerpath/container_rsa.pub >> ~/.ssh/authorized_keys
echo "127.0.0.1   build01.localhost" >> /etc/hosts
