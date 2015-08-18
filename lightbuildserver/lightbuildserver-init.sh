#!/bin/bash

chown -R uwsgi:uwsgi /usr/share/lightbuildserver/
chown -R uwsgi:uwsgi /var/lib/lightbuildserver/
chown uwsgi:uwsgi /etc/uwsgi.d/lightbuildserver.ini
usermod -a nginx -G uwsgi
touch /var/log/uwsgi.log
chown uwsgi:uwsgi /var/log/uwsgi.log
touch /var/log/lbs.log
chown uwsgi:uwsgi /var/log/lbs.log

# disable the default page by moving it to port 81
sed -i "s/80 default_server/81 default_server/g" /etc/nginx/nginx.conf

etccontainerpath=/etc/lightbuildserver/container
echo "this key will be used to login to the host for the containers."
echo "leave the passwort empty!"
mkdir -p $etccontainerpath
ssh-keygen -t rsa -f $etccontainerpath/container_rsa
chown -R uwsgi:uwsgi $etccontainerpath

# enable and start nginx and uwsgi
systemctl enable nginx
systemctl start nginx
systemctl enable uwsgi
systemctl start uwsgi

# enable the cronjob for processing the build queue
crontab -u uwsgi -l | { cat; echo "# every minute, execute this loop to process the build queue"; echo "* * * * * for i in \`seq 1 11\`; do wget -q http://localhost/processbuildqueue -O /tmp/lbsqueue > /dev/null; rm -f /tmp/lbsqueue; sleep 5; done"; } | crontab -u uwsgi -
systemctl enable crond
systemctl start crond

# for using the local machine as a host for the containers
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh/authorized_keys
cat $etccontainerpath/container_rsa.pub >> ~/.ssh/authorized_keys
echo "127.0.0.1   build01.localhost" >> /etc/hosts
