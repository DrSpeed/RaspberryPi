#!/bin/sh
#DATE_STR=$(date -u +\%Y-\%m-\%d)
# milliseconds since epoch
DATE_STR=$(date +\%s\%3N)
HOUR_STR=$(date +\%H)


curl -XGET -s "http://auto2-report-dev-1.globix-sc.gracenote.com:9200/iot_index/_search" \ 
       "{ \"query\" : {                        \
	    \"match\" : {                      \
           	\"room\" : \"client_engg\",    \
	    }                                  \
        }}"



