#!/bin/sh
DATE_STR=$(date +\%Y-\%m-\%d)
echo $DATE_STR
cat /home/pi/git/RaspberryPi/date_template.xml | sed  -e 's/date_alias/'"$DATE_STR"'/g' > /tmp/today.xml

cat /home/pi/git/RaspberryPi/metro_date_template.xml | sed  -e 's/date_alias/'"$DATE_STR"'/g' > /tmp/metro_today.xml

# generate the (exchng_meeting) xml file that has all the meeting data
curl -u swinter@gracenote:<pwd> -L https://mailhost.gracenote.gracenote.com/ews/exchange.asmx -H "Content-Type:text/xml" --data "@/tmp/today.xml" --ntlm > /tmp/samp.xml; xmllint --format /tmp/samp.xml > /tmp/exchng_meeting_data.xml


curl -u swinter@gracenote:<pwd> -L https://mailhost.gracenote.gracenote.com/ews/exchange.asmx -H "Content-Type:text/xml" --data "@/tmp/metro_today.xml" --ntlm > /tmp/metro_samp.xml; xmllint --format /tmp/metro_samp.xml > /tmp/metro_exchng_meeting_data.xml

#write meeting report to an html file
xsltproc /home/pi/git/RaspberryPi/ewsToHtml.xsl /tmp/exchng_meeting_data.xml > /var/www/html/today.html

xsltproc /home/pi/git/RaspberryPi/ewsToHtml.xsl /tmp/metro_exchng_meeting_data.xml > /var/www/html/metro_today.html

# --Write it to elastic search db--
# Compose to shell script
xsltproc /home/pi/git/RaspberryPi/ewsToInsert.xsl /tmp/exchng_meeting_data.xml > /tmp/ewsToInsert.sh
# enable as executeable
chmod +x /tmp/ewsToInsert.sh
# execute the elastic search insert
/tmp/ewsToInsert.sh

xsltproc /home/pi/git/RaspberryPi/ewsToXml.xsl /tmp/exchng_meeting_data.xml > /tmp/simple_meeting_data.xml
xsltproc /home/pi/git/RaspberryPi/ewsToXml.xsl /tmp/metro_exchng_meeting_data.xml > /tmp/metro_meeting_data.xml


/usr/bin/python /home/pi/git/RaspberryPi/pyxml.py -i /tmp/simple_meeting_data.xml -o /var/www/html/meeting_table.html -t Room_Client_Engineering
/usr/bin/python /home/pi/git/RaspberryPi/pyxml.py -i /tmp/metro_meeting_data.xml -o /var/www/html/metro_meeting_table.html -t Room_Metropolis
