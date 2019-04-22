import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)
switch=False

for i in range(3):
    switch=input()
    if switch==True:
        print("switching")
        GPIO.output(19,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(19,GPIO.LOW)
    else:
        print("not switching")