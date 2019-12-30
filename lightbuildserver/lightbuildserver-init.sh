#!/bin/bash

pip3 install gunicorn
pip3 install gunicorn[gevent]

useradd lbs
usermod -a nginx -G lbs
touch /var/log/lbs.log
chown lbs:lbs /var/log/lbs.log

# disable the default page by moving it to port 81
sed -i "s/80 default_server/81 default_server/g" /etc/nginx/nginx.conf

etccontainerpath=/etc/lightbuildserver/container
if [ ! -f $etccontainerpath/container_rsa ]
then
  echo "this key will be used to login to the host for the containers."
  echo "leaving the passwort empty!"
  mkdir -p $etccontainerpath
  ssh-keygen -t rsa -f $etccontainerpath/container_rsa -P ""
  chown -R lbs:lbs $etccontainerpath

  # for using the local machine as a host for the containers
  mkdir -p ~/.ssh
  chmod 700 ~/.ssh
  echo >> ~/.ssh/authorized_keys
  chmod 700 ~/.ssh/authorized_keys
  cat $etccontainerpath/container_rsa.pub >> ~/.ssh/authorized_keys
  echo "127.0.0.1   build01.localhost" >> /etc/hosts
fi

# enable and start nginx and lbs
systemctl enable nginx
systemctl start nginx
systemctl enable lbs
systemctl start lbs

# enable and start mariadb
systemctl enable mariadb
systemctl start mariadb

# enable the cronjob for processing the build queue
if [ -z "`crontab -u uwsgi -l | grep 'process the build queue'`" ]
then
  crontab -u uwsgi -l | { cat; echo "# every minute, process the build queue"; echo "* * * * * /usr/share/lightbuildserver/cron.sh"; } | crontab -u uwsgi -
fi
systemctl enable crond
systemctl start crond
