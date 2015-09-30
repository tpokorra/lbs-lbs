#!/bin/sh

jobruns=`ps xaf | grep -v grep | grep processbuildqueue`
if [ -z "$jobruns" ]
then
  ip4=`ip addr list eth0 | grep "inet "|cut -d' ' -f6|cut -d/ -f1`
  for i in `seq 1 6`
  do
    wget --tries=1 --timeout=3 -q http://${ip4}/processbuildqueue -O /dev/null > /dev/null
    sleep 5
  done
fi
