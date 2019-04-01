import RPi.GPIO as GPIO
import time 
out1=13
out2=11
out3=15
out4=12
def MotorAssign(ot1,ot2,ot3,ot4):
    out1=ot1
    out2=ot2
    out3=ot3
    out4=ot4
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(out1,GPIO.OUT)
    GPIO.setup(out2,GPIO.OUT)
    GPIO.setup(out3,GPIO.OUT)
    GPIO.setup(out4,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    GPIO.setup(35,GPIO.OUT)
    GPIO.output(37,GPIO.HIGH)
    GPIO.output(35,GPIO.HIGH)
#just a thing for running a motor
def MotorRun():
    i=0
    positive=0
    negative=0
    y=0
    x = input()
    x=x*400
    if x<=400:
        convstep(x)
    else:
        z=x%400
        x=x-z
        convstep(z)
        z=x/400
        while(z>0):
            convstep(400)
            z=z-1

def convstep(x):
    negative =0
    i=0
    positive =0
    y=0

    if(x==0):
        return
    try:
        while(1):
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            if x>0 and x<=400:
                print ("inside  loop")
                for y in range(x,0,-1):
                    if negative==1:
                        if i==7:
                            i=0
                        else:
                            i=i+1
                        y=y+2
                        negative=0
                    positive=1
                    #print((x+1)-y)
                    if i==0:
                        GPIO.output(out1,GPIO.HIGH)
                        GPIO.output(out2,GPIO.LOW)
                        GPIO.output(out3,GPIO.LOW)
                        GPIO.output(out4,GPIO.LOW)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==1:
                        GPIO.output(out1,GPIO.HIGH)
                        GPIO.output(out2,GPIO.HIGH)
                        GPIO.output(out3,GPIO.LOW)
                        GPIO.output(out4,GPIO.LOW)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==2:  
                        GPIO.output(out1,GPIO.LOW)
                        GPIO.output(out2,GPIO.HIGH)
                        GPIO.output(out3,GPIO.LOW)
                        GPIO.output(out4,GPIO.LOW)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==3:    
                        GPIO.output(out1,GPIO.LOW)
                        GPIO.output(out2,GPIO.HIGH)
                        GPIO.output(out3,GPIO.HIGH)
                        GPIO.output(out4,GPIO.LOW)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==4:  
                        GPIO.output(out1,GPIO.LOW)
                        GPIO.output(out2,GPIO.LOW)
                        GPIO.output(out3,GPIO.HIGH)
                        GPIO.output(out4,GPIO.LOW)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==5:
                        GPIO.output(out1,GPIO.LOW)
                        GPIO.output(out2,GPIO.LOW)
                        GPIO.output(out3,GPIO.HIGH)
                        GPIO.output(out4,GPIO.HIGH)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==6:    
                        GPIO.output(out1,GPIO.LOW)
                        GPIO.output(out2,GPIO.LOW)
                        GPIO.output(out3,GPIO.LOW)
                        GPIO.output(out4,GPIO.HIGH)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==7:    
                        GPIO.output(out1,GPIO.HIGH)
                        GPIO.output(out2,GPIO.LOW)
                        GPIO.output(out3,GPIO.LOW)
                        GPIO.output(out4,GPIO.HIGH)
                        time.sleep(0.03)
                        #time.sleep(1)
                    if i==7:
                        i=0
                        continue
                    i=i+1
            
            
            elif x<0 and x>=-400:
                x=x*-1
                for y in range(x,0,-1):
                    if positive==1:
                        if i==0:
                            i=7
                        else:
                            i=i-1
                        y=y+3
                        positive=0
                    negative=1
                    #print((x+1)-y) 
                    if i==0:
                        GPIO.output(out1,GPIO.HIGH)
                        GPIO.output(out2,GPIO.LOW)
                        GPIO.output(out3,GPIO.LOW)
                        GPIO.output(out4,GPIO.LOW)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==1:
                        GPIO.output(out1,GPIO.HIGH)
                        GPIO.output(out2,GPIO.HIGH)
                        GPIO.output(out3,GPIO.LOW)
                        GPIO.output(out4,GPIO.LOW)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==2:  
                        GPIO.output(out1,GPIO.LOW)
                        GPIO.output(out2,GPIO.HIGH)
                        GPIO.output(out3,GPIO.LOW)
                        GPIO.output(out4,GPIO.LOW)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==3:    
                        GPIO.output(out1,GPIO.LOW)
                        GPIO.output(out2,GPIO.HIGH)
                        GPIO.output(out3,GPIO.HIGH)
                        GPIO.output(out4,GPIO.LOW)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==4:  
                        GPIO.output(out1,GPIO.LOW)
                        GPIO.output(out2,GPIO.LOW)
                        GPIO.output(out3,GPIO.HIGH)
                        GPIO.output(out4,GPIO.LOW)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==5:
                        GPIO.output(out1,GPIO.LOW)
                        GPIO.output(out2,GPIO.LOW)
                        GPIO.output(out3,GPIO.HIGH)
                        GPIO.output(out4,GPIO.HIGH)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==6:    
                        GPIO.output(out1,GPIO.LOW)
                        GPIO.output(out2,GPIO.LOW)
                        GPIO.output(out3,GPIO.LOW)
                        GPIO.output(out4,GPIO.HIGH)
                        time.sleep(0.03)
                        #time.sleep(1)
                    elif i==7:    
                        GPIO.output(out1,GPIO.HIGH)
                        GPIO.output(out2,GPIO.LOW)
                        GPIO.output(out3,GPIO.LOW)
                        GPIO.output(out4,GPIO.HIGH)
                        time.sleep(0.03)
                        #time.sleep(1)
                    if i==0:
                        i=7
                        continue
                    i=i-1 
    except KeyboardInterrupt:
        GPIO.cleanup()  

MotorAssign(out1,out2,out3,out4)
MotorRun()
