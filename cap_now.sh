#!/bin/bash 


fswebcam -s --jpeg 90 -r 640x480 -d /dev/video0 webcam.jpg

HOST=ftp.XXX
USER=XXX
PASS=XXX

ftp -inv $HOST <<EOF
EOF 
user $USER $PASS 
put webcam.jpg
bye 
EOF
