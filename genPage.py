#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from datetime import datetime

con = None

#-- files --
filename = '/home/pi/node/report.html'
db = '/home/pi/sqlite/camera_db'
#---

def renderRow(dateData):
    target.write('<tr>')
    target.write('<td width="4%">{0}</td>'.format(dateData))
    for x in xrange(0, 24):
        hourstr = "{:0>2}".format(x)
        sql = 'select CAST(sum(duration) AS FLOAT) from pic_event where pdate == date(\'{0}\') and strftime(\'%H\', time(ptime)) = \'{1}\';'.format(dateData, hourstr);
        #print sql
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows: # There should only be one row
            #print row[0].__class__

            f = row[0]
            if row[0] is None:
                rowstr = '    '
                bgc = '#FFFFFF' # white
            else :
                rowstr = "{0:.2f}".format(f)
                bgc = '#66ccff'

            target.write('<td width="4%" bgcolor="{1}">{0}</td>'.format(rowstr, bgc))

    target.write('</tr>')
    return


try:
    con = lite.connect(db)
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()
    target = open(filename, 'w')  # output file

    target.truncate()
    target.write('<html><head></head><body>')
    #header stuff
    target.write('Report generated at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '<br>')
    target.write('SQLite version: {0}'.format(data))

    
    target.write ('<link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css">')
    cur.execute("select pdate from pic_event group by pdate;")

    target.write('<style>table, th, td { border: 1px solid black; }</style>')
    
    rows = cur.fetchall()
    target.write('<div style="width:25%; class="w3-container">');
    target.write('<h3>Motion Profile</h3>');
#    target.write('<table class="w3-table w3-bordered w3-striped">')
#    target.write('<tr><td>Date</td><td>Time</td></tr>');

    target.write('<table class="w3-table w3-bordered w3-striped">')

    target.write('<tr>')
    # hour header
    target.write('<td width="4%">Date</td>')
    for x in xrange(0, 24):
        hourstr = "{:0>2}".format(x)
        target.write('<td width="4%" bgcolor="gray">{0}</td>'.format(hourstr))
    target.write('</tr>')


    for row in rows:
        renderRow(row[0])

    target.write('</table>')

    target.write('</div">');
    target.write('</body></html>')
    target.close()
except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()

print 'updated report page'         
