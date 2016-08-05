import subprocess
import shutil
import time
import os
import RPi.GPIO as io
import sqlite3 as lite
import time


ledpin = 17
pir_pin = 4


# set up GPIO
io.setmode(io.BCM)
io.setmode(io.BCM)
io.setwarnings(False)
io.setup(ledpin, io.OUT)    # led
io.setup(pir_pin, io.IN)    # activate input

#--files--
db = '/home/pi/sqlite/camera_db'
capshell = '/home/pi/node/capture.sh'
#---

motionState = False;

MAX_TIME = 3600  #Avoid odd time issues after reboot


while True:
    if io.input(pir_pin):
        if motionState == False:
            print("PIR ALARM!")
            motionState = True;
            start = time.time()
            io.output(ledpin, io.HIGH)
            #os.system('sudo ' + capshell)
    else:
        if motionState == True:
            print("PIR OFF!")
            end = time.time()
            delta = (end - start)
            delta = min(delta, MAX_TIME) 
            print('Time diff: ')
            print(delta)
            con = lite.connect(db)
            con.execute('INSERT INTO pic_event VALUES (date(\'now\', \'localtime\'), time(\'now\', \'localtime\'), {0});'.format(delta))
            con.commit()
            io.output(ledpin, io.LOW)
            motionState = False;
    time.sleep(1.0)
