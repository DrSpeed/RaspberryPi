import RPi.GPIO as GPIO
import time
import os



GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

isOne = True
isTwo = False
isFour = False

while True:
  if  isOne == True:
      isOne = False
      GPIO.output(17, True)
      isTwo = True
      GPIO.output(27, False)
  elif isTwo == True:
      isTwo = False
      GPIO.output(27, True)
      isFour = True
      GPIO.output(4, False)
  else:
      isFour = False
      GPIO.output(4, True)
      isOne = True
      GPIO.output(17, False)
 
  time.sleep(1)
