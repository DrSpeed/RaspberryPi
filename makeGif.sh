#!/bin/sh
#Compose date string, possibly used in image filename
DATE_STR=$(date +\%a_\%H_\%M_\%p)


#create an animated gif from all the thumbnail images
convert -delay 20 -loop 0 /var/www/html/img/capture_*th.jpg /var/www/html/yesterday.gif

