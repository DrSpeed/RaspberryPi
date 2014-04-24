#!/bin/bash 

HOST=XXX
USER=XXX
PASS=XXX

# USB webcam (Serial)
FILENAME_STUB=webcam3_
# Raspberry Pi Still camera (Parallel)
PI_CAM_STUB=picam_
TMP_IMG=eraseme.jpg
day_tail=$(date "+%H_%M")
hour_tail=$(date "+%M")

# Compose filenames
day_filename=$FILENAME_STUB$day_tail.jpg
hour_filename=$FILENAME_STUB$hour_tail.jpg

rps_day_filename=$PI_CAM_STUB$day_tail.jpg
rps_hour_filename=$PI_CAM_STUB$hour_tail.jpg

# Take image with parallel camera
sudo raspistill -o $TMP_IMG -n -w 1280 -h 1024 -e 

banner="   Raspberry Pi Camera:"$(date "+%a %Y/%m/%e %l:%M%P")"   "

# convert program inconsistent results if you use the same name for input and output, use temp file
convert $TMP_IMG  -undercolor '#0008' -pointsize 50 -fill red -annotate +100+100  "$banner" $rps_hour_filename

rm -rf $TMP_IMG

# smaller 'hour' one for site
#sudo raspistill -o $hour_filename -w 640 -h 480

# Take images with USB Camera
fswebcam -c /home/pi/.fswebcam.conf -r 640x480 -d /dev/video0 $hour_filename

ftp -inv $HOST <<EOF
EOF                                                            
EOF                                                                             
user $USER $PASS                                                                
put $hour_filename
put $rps_hour_filename
bye                                                                             

EOF                      
EOF

# Copy to web folders (day & hour)

#-------------------------------------------
# USB Camera (Serial)
# Copy to daily with new name
cp -f $hour_filename      /var/www/dayImages/$day_filename
# Move it to hourly
mv -f $hour_filename     /var/www/hourImages/$hour_filename

#-------------------------------------------
# Raspberry Pi Camera (parallel)
# Copy to daily with new name
cp -f $rps_hour_filename  /var/www/dayImages/$rps_day_filename
# Move it to hourly
mv -f $rps_hour_filename /var/www/hourImages/$rps_hour_filename


# Play a sound
#mpg321 /home/pi/sounds/Drop_FX02.mp3  -l 2 -q -g 25


