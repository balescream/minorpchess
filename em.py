import RPi.GPIO as GPIO
import time

out1=16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
switch=False

try:
    while 1:
        switch=input()
        if switch==True:
            print("off")
            GPIO.output(out1,GPIO.HIGH)
        else:
            print("on")
            GPIO.output(out1,GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()