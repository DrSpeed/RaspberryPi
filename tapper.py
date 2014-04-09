import RPi.GPIO as GPIO
import time
import os
import random


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
      GPIO.output(27, True)
      GPIO.output(4, False)
  else:
      isOne = True
      GPIO.output(27, False)
      GPIO.output(4, True)
  timeRand = random.randint(0, 8)      
  time.sleep(timeRand)
