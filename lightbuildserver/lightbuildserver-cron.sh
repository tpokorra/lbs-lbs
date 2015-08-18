#!/bin/sh

jobruns=`ps xaf | grep -v grep | grep processbuildqueue`
if [ -z "$jobruns" ]
then
  for i in `seq 1 6`
  do 
    wget --tries=1 --timeout=3 -q http://localhost/processbuildqueue -O /dev/null > /dev/null
    sleep 5
  done
fi
