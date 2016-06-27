#!/bin/sh
#DATE_STR=$(date -u +\%Y-\%m-\%d)
# milliseconds since epoch
DATE_STR=$(date +\%s\%3N)
HOUR_STR=$(date +\%H)

#curl -XPOST -s "http://swinter-06348:19200/event/hack" -d "{\"room\":\"clientEng\", \"duration\":$1, \"event_day\":\"${DATE_STR}\", \"event_hour\":${HOUR_STR} }"

#DATE_STR="2016-07-04"

echo $DATE_STR
echo $HOUR_STR

#curl -XPOST -s "http://auto2-report-dev-1.globix-sc.gracenote.com:9200/iot_index/iot" -d "{\"room\" : \"client_engg\", \"date\": \"${DATE_STR}\", \"hour\" : \"${HOUR_STR}\", \"duration\": $1 }"

curl -XPOST -s "http://auto2-report-dev-1.globix-sc.gracenote.com:9200/iot_index/iot" \
     -d "{\"room\" :  \"client_engg\", \
          \"date\":     ${DATE_STR},   \
          \"hour\" :  \"${HOUR_STR}\", \
          \"duration\": $1 }"






