import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)
switch=False

try:
    while 1:
        switch=input()
        if switch==True:
            print("off")
            GPIO.output(19,GPIO.HIGH)
        else:
            print("on")
            GPIO.output(19,GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()