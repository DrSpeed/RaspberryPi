import time
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 4


io.setup(pir_pin, io.IN)         # activate input


while True:
    if io.input(pir_pin):
        print("PIR ALARM!")
    else:
        print("PIR OFF!")
    time.sleep(1.0)
