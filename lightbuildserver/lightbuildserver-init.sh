#!/bin/bash

usermod -a nginx -G uwsgi
touch /var/log/uwsgi-req.log
chown uwsgi:uwsgi /var/log/uwsgi-req.log
touch /var/log/uwsgi.log
chown uwsgi:uwsgi /var/log/uwsgi.log
touch /var/log/lbs.log
chown uwsgi:uwsgi /var/log/lbs.log

# disable the default page by moving it to port 81
sed -i "s/80 default_server/81 default_server/g" /etc/nginx/nginx.conf

etccontainerpath=/etc/lightbuildserver/container
if [ ! -f $etccontainerpath/container_rsa ]
then
  echo "this key will be used to login to the host for the containers."
  echo "leave the passwort empty!"
  mkdir -p $etccontainerpath
  ssh-keygen -t rsa -f $etccontainerpath/container_rsa
  chown -R uwsgi:uwsgi $etccontainerpath

  # for using the local machine as a host for the containers
  mkdir -p ~/.ssh
  chmod 700 ~/.ssh
  echo >> ~/.ssh/authorized_keys
  chmod 700 ~/.ssh/authorized_keys
  cat $etccontainerpath/container_rsa.pub >> ~/.ssh/authorized_keys
  echo "127.0.0.1   build01.localhost" >> /etc/hosts
fi

# enable and start nginx and uwsgi
systemctl enable nginx
systemctl start nginx
systemctl enable uwsgi
systemctl start uwsgi

# enable the cronjob for processing the build queue
if [ -z "`crontab -u uwsgi -l | grep 'process the build queue'`" ]
then
  crontab -u uwsgi -l | { cat; echo "# every minute, process the build queue"; echo "* * * * * /usr/share/lightbuildserver/cron.sh"; } | crontab -u uwsgi -
fi
systemctl enable crond
systemctl start crond
