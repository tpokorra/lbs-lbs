#!/bin/sh

jobruns=`ps xaf | grep -v grep | grep processbuildqueue`
if [ -z "$jobruns" ]
then
  ip4=`/usr/sbin/ip addr list eth0 | grep "inet "|cut -d' ' -f6|cut -d/ -f1`
  for i in `seq 1 6`
  do
    # need to check both addresses.
    # when starting the server locally, it listens on the external IP address.
    # uwsgi listens on localhost
    for ip in $ip4 localhost
    do
      wget --tries=1 --timeout=3 -q http://${ip}/processbuildqueue -O /dev/null > /dev/null
    done
    sleep 5
  done
fi
