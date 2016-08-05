#!/usr/bin/python
from lxml import etree

import sys, getopt

def main(argv):
   startIn = ''
   endIn = ''
   dateIn = ''
   try:
      opts, args = getopt.getopt(argv,"hs:e:d:",["start=","end=","date="])
   except getopt.GetoptError:
      print 'pycurl.py -s <start> -e <end> -d <date>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'pycurl.py -s <start> -e <end> -d <date>'
         sys.exit()
      elif opt in ("-s", "--start"):
         startIn = arg
      elif opt in ("-e", "--end"):
         endIn = arg
      elif opt in ("-d", "--date"):
         dateIn = arg
   print 'Start is "', startIn
   print 'End   is   "', endIn
   print 'Date  is   "', dateIn

   startSplit = startIn.split(":")
   endSplit = endIn.split(":")
   startHr = int(startSplit[0])
   endHr = int(endSplit[0])
   startMin = int(startSplit[1])
   endMin = int(endSplit[1])

   print 'Start hr', startHr
   print 'End   hr', endHr

   print 'Start hr_min', startHr * 60
   print 'End   hr_min', endHr *60

   print 'Start total min', (startHr * 60) + startMin
   print 'End   total min', (endHr * 60) + endMin

   totalDuration = ((endHr * 60) + endMin) - ((startHr * 60) + startMin)
   print 'Total Min: ', totalDuration

   hrCount = 0
   while (totalDuration > 60):
      print 'one hour', startHr + hrCount, ' to ', startHr + hrCount + 1
      totalDuration -= 60
      hrCount += 1

   print 'Minutes ', totalDuration

   totalHrs = 12
   curHr = 0
   hrOffset = 8
   while(curHr < totalHrs):
      print 'Time is ', curHr + hrOffset
      curHr += 1
      

   
if __name__ == "__main__":
   main(sys.argv[1:])
