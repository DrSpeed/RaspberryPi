#!/usr/bin/python
import xml.etree.ElementTree as ET
import sys, getopt
from datetime import datetime

celSubject = ''  # yuck, a global hack here

class Event:

   def __init__(self):
      self.date     = ""
      self.startHr  = ""
      self.startMin = ""
      self.endHr    = ""
      self.endMin   = ""
      self.subject  = ""


   def printit(self):
      print 'date: '    , self.date
      print 'startHr: ' , self.startHr
      print 'startMin: ', self.startMin
      print 'endHr: '   , self.endHr
      print 'endMin: '  , self.endMin
      print 'subject: ' , self.subject

def timeReserved(hour, minute, events):
   for ev in events:
      if (eventTimeSameOrBefore(ev.startHr, ev.startMin, hour, minute) == True) and \
         (eventTimeAfter(ev.endHr, ev.endMin, hour, minute) == True):
         #print '--True reserved: ', ev.printit(), "-", hour, ":", minute
         #ev.printit()
         global celSubject
         celSubject = ev.subject
         return True

   return False

          
def eventTimeSameOrBefore(eventHr, eventMin, timeHr, timeMin):
   #print 'same/before (event/time) ', eventHr, ":", eventMin, "  ", timeHr, ":", timeMin

   eventTotalMin = (eventHr * 60) + eventMin
   timeTotalMin = (timeHr * 60) + timeMin

   if eventTotalMin <= timeTotalMin:
      return True
   return False

def eventTimeAfter(eventHr, eventMin, timeHr, timeMin):
   #print 'same/after (event/time) ', eventHr, ":", eventMin, "  ", timeHr, ":", timeMin
   eventTotalMin = (eventHr * 60) + eventMin
   timeTotalMin = (timeHr * 60) + timeMin

   if eventTotalMin > timeTotalMin:
      #print 'true'
      return True
   return False
 
      
def main(argv):
   infilename = ''
   outfilename = ''
   title=''
   try:
      opts, args = getopt.getopt(argv,"hi:o:t:",["input=", "output","title"])
   except getopt.GetoptError:
      print 'pyxml.py -i <xmlfile> -o <htmlfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'pyxml.py -f <file>'
         sys.exit()
      elif opt in ("-i", "--input"):
         infilename = arg
      elif opt in ("-o", "--output"):
         outfilename = arg
      elif opt in ("-t", "--title"):
         title = arg

   tree = ET.parse(infilename)
   root = tree.getroot()

   myEvents=[]
   
   for child in root:
      e = Event()
      e.date =  child[0].text
      startStr= child[1].text
      endStr  =  child[2].text
      subject = child[3].text
      
      startSplit = startStr.split(":")
      endSplit = endStr.split(":")

      startHr = int(startSplit[0])
      startMin = int(startSplit[1])
      endHr = int(endSplit[0])
      endMin = int(endSplit[1])

      e.startHr = startHr
      e.startMin = startMin
      e.endHr = endHr
      e.endMin = endMin
      e.subject = subject
      #e.printit()
      myEvents.append(e)

   #print 'n envents: ', len(myEvents)


   target = open(outfilename, 'w')  # output file
   target.write('<html><head></head><body>')
   target.write('<link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css">')
   target.write('<style>table, th, td { border: 1px solid #232323;font-size:8pt; }</style>')
   target.write('Report generated at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '<br>')
   target.write('<h3>Meeting Room <u>' + title + '</u></h3>');
   target.write('<h4>Room Schedule For: ')
   target.write(myEvents[0].date)
   target.write('</h4>')
   target.write('<H4>Actual Room Usage</H4>');
   target.write('<div>')
   target.write('<iframe src="http://auto2-report-dev-1.globix-sc.gracenote.com:5601/app/kibana#/dashboard/iot_demo?embed=true&_g=(refreshInterval:(display:Off,pause:!f,value:0),time:(from:now-15m,mode:quick,to:now))&_a=(filters:!(),options:(darkTheme:!f),panels:!((col:1,id:iot_duration,panelIndex:2,row:3,size_x:12,size_y:3,type:visualization),(col:1,id:iot_duration_daily,panelIndex:3,row:1,size_x:12,size_y:2,type:visualization)),query:(query_string:(analyze_wildcard:!t,query:\'*\')),title:iot_demo,uiState:(P-2:(spy:(mode:(fill:!f,name:!n))),P-3:(vis:(legendOpen:!f))))" height="600" width="900"></iframe>');
   target.write('</div>')


   target.write('<div style="width:50%;" class="w3-container" >')
   #header stuff
   target.write('<H4>Scheduled Room Usage</H4>');
   target.write('<table class="w3-table w3-bordered w3-striped">')
   target.write('<tr height="100px">')
   target.write('<td>Room Status</td>')
   for h in range(8, 20):
      for m in range(0, 4):
         global celSubject
         
         target.write('\n')
         timeMin = m * 15
         isReserved = timeReserved(h, timeMin, myEvents)

         titleStr = 'busy'
         if m==0 and isReserved:
            titleStr = celSubject
            target.write('<td width="20px" title="' + titleStr + '" bgcolor="#3399ff">')
         elif isReserved:
            titleStr = celSubject
            target.write('<td width="20px" title="' + titleStr + '" bgcolor="#6699ff">')
         elif m==0:
            titleStr = 'free'
            target.write('<td width="20px" title="' + titleStr + '" bgcolor="#ffcc99">')
         else:
            titleStr = 'free'
            target.write('<td width="20px" title="' + titleStr + '" bgcolor="white">')

            target.write(' ')
         target.write('</td>')
   target.write('</tr>')

   # lower 'hours' table
   target.write('<tr>')

   target.write('<td>Time</td>')
   for h in range(8, 20):
      for m in range(0, 4):
         target.write('\n')
         timeMin = m * 15
         
         titleStr = "%d to %d" % (h, h+1)

         if m==0:
            target.write('<td colspan="4" width="20px" title="' + titleStr + '"  bgcolor="#ffcc99">')

         if m == 0:
            lbl = h
            if lbl > 12:
               lbl -= 12
            target.write(titleStr)
         else: 
            target.write(' ')
            
         target.write('</td>')
   target.write('</tr>')

   target.write('</table>')

   target.write('</div">');

   target.write('Other Rooms:<br>')
   target.write('<a href="http://raspberrypi2/metro_meeting_table.html">Room Metropolis Availability</a>')
   target.write('<br>')
   target.write('<a href="http://raspberrypi2/meeting_table.html">Room Client Engineering Availability</a>')
   


   target.write('</body></html>')
   target.close()



   
      
if __name__ == "__main__":
   main(sys.argv[1:])
