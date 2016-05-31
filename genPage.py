#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from datetime import datetime
import matplotlib.colors as colors

MAX_TIME = 2000.0

con = None

#-- files --
filename = '/home/pi/node/report.html'
db = '/home/pi/sqlite/camera_db'
#---

def rgb_to_hex(rgb_tuple):
    return colors.rgb2hex([1.0*x/255 for x in rgb_tuple])

def convert_to_rgb(minval, maxval, val, colors):
    max_index = len(colors)-1
    v = float(val-minval) / float(maxval-minval) * max_index
    i1, i2 = int(v), min(int(v)+1, max_index)
    (r1, g1, b1), (r2, g2, b2) = colors[i1], colors[i2]
    f = v - i1
    return rgb_to_hex( (int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))))

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

            nSeconds = row[0]
            if row[0] is None:
                rowstr = '    '
                bgc = '#FFFFFF' # white
            else :
                c = [ (230, 230, 255), (255, 153, 0), (255, 255, 0)]  # [BLUE, GREEN, RED]
                nSeconds = min(MAX_TIME, nSeconds)
                rowstr = "{0:.0f}".format(nSeconds)
                //print "Secs: " + rowstr
                bgc =  convert_to_rgb( 0, MAX_TIME, nSeconds, c)

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
        target.write('<td width="80px" bgcolor="gray">{0}</td>'.format(hourstr))
    target.write('</tr>')

    print "rendering rows..."
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
