import RPi.GPIO as GPIO
import time
import os



GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)


GPIO.output(17, True)
GPIO.output(27, True)
GPIO.output(4, True)

