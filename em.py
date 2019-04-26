
import RPi.GPIO as GPIO
import time

out1=16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
state=False
while 1:
	state=input()
	if state:
		print("on")
		GPIO.output(out1,GPIO.HIGH)
	else:
		print("off")
		GPIO.output(out1,GPIO.LOW)
