#!/bin/sh
DATE_STR=$(date +\%a_\%H_\%M_\%p)
/usr/bin/raspistill -n -o  /home/pi/node/img/capture_${DATE_STR}.jpg
/usr/bin/raspistill -n -w 128 -h 128 -o  /home/pi/node/img/capture_${DATE_STR}_th.jpg
