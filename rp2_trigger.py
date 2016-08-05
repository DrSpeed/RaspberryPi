import subprocess
import shutil
import time
import os
import RPi.GPIO as io
import sqlite3 as lite
import time

# Put this in:  /etc/rc.local at end, before exit

# set up GPIO
io.setmode(io.BCM)
pir_pin = 4

#--files--
db = '/home/pi/sqlite/camera_db'
capshell = '~pi/git/RaspberryPi/PostToElastic.sh'
#---

motionState = False;

io.setup(pir_pin, io.IN)         # activate input


while True:
    if io.input(pir_pin):
        if motionState == False:
            print("PIR ALARM!")
            motionState = True;
            start = time.time()

    else:
        if motionState == True:
            print("PIR OFF!")
            end = time.time()
            delta = (end - start)
            deltaStr = "{:0>0}".format(delta)
            deltaInt = int(delta)
            print('Time diff: ')
            print(deltaInt)
            os.system('sudo ' + capshell + ' ' + str(deltaInt))
            motionState = False;
    time.sleep(1.0)
