import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)
switch=False

for i in range(3):
    switch=input()
    if switch==True:
        print("off")
        GPIO.output(19,GPIO.HIGH)
        time.sleep(0.5)
    else:
        print("on")
        GPIO.output(19,GPIO.LOW)