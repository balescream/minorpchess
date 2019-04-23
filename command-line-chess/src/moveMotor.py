from motor1 import rotatemotor as rotateY
from motor2 import rotatemotor as rotateX
from em import toggleMagnet as toggleMagnet

motorcurentx = 0
motorcurenty = 0

xscale = 3
yscale = 3

def moveMotor(move):
    convertMove(move)

def trackInitial(x2,y2):
	moveX(x2,0)
	moveY(y2,0)

def moveX(x1, x2):
    dx = x2-x1
    rotateX(dx*xscale)

def moveY(y1, y2):
    dy = y2-y1
    rotateY(-1*dy*yscale)


def moveToOldPos(x1, y1):
    moveX(0,x1)
    moveY(0,y1)
    print("current position "+str(x1) +" "+str(y1))
    print("picking the peice up")
    toggleMagnet(True)

def moveToNewPos(x1,y1,x2,y2):
    moveX(x1,x2)
    moveY(y1,y2)
    print("current position "+str(x2) +" "+str(y2))
    print("dropping the piece moving towards zero");
    toggleMagnet(False)
    moveMotortozero(x2,y2)

def moveMotortozero(x,y):
    moveX(x,0)
    moveY(y,0)
    print("finally at zero")

def convertMove(move):
    print("inside the motor")
    x1 = move.oldPos[0]
    y1 = move.oldPos[1]
    x2 = move.newPos[0]
    y2 = move.newPos[1]
    print("current position 0,0")
    moveToOldPos(x1,y1)
    moveToNewPos(x1,y1,x2,y2)

