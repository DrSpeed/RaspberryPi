import subprocess
import shutil
import time
import os
import RPi.GPIO as io
import sqlite3 as lite
import time

# set up GPIO
io.setmode(io.BCM)
pir_pin = 4

#--files--
db = '/home/pi/sqlite/camera_db'
capshell = '/home/pi/node/capture.sh'
#---

motionState = False;

io.setup(pir_pin, io.IN)         # activate input


while True:
    if io.input(pir_pin):
        if motionState == False:
            print("PIR ALARM!")
            motionState = True;
            start = time.time()
            #os.system('sudo ' + capshell)
    else:
        if motionState == True:
            print("PIR OFF!")
            end = time.time()
            delta = (end - start)
            print('Time diff: ')
            print(delta)
            con = lite.connect(db)
            con.execute('INSERT INTO pic_event VALUES (date(\'now\', \'localtime\'), time(\'now\', \'localtime\'), {0});'.format(delta))
            con.commit()
            motionState = False;
    time.sleep(1.0)
