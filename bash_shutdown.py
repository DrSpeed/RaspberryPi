import RPi.GPIO as GPIO
import time
import os

#insert switch between board pin 1 and 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
while True:
  if  GPIO.input(4) == False:
    print "false"
  else:
    print "true"
  time.sleep(1)
