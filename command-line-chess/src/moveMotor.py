from motor1 import rotatemotor as rotateY
from motor2 import rotatemotor as rotateX

motorcurentx = 0
motorcurenty = 0

xscale = 1
yscale = 1

def moveMotor(move):
    convertMove(move)

# def trackToInitial():
#     #TODO  
    
def moveX(x1, x2):
    dx = x2-x1
    rotateX(dx*xscale)

def moveY(y1, y2):
    dy = y2-y1
    rotateY(dy*yscale)


def moveToOldPos(x1, y1):
    moveX(0,x1)
    moveY(0,y1)
    toggleMagnet(True)

def moveToNewPos(x1,y1,x2,y2):
    moveX(x1,x2)
    moveY(y1,y2)
    toggleMagnet(False)
    moveMotortozero(x2,y2)

def moveMotortozero(x,y):
    moveX(x,0)
    moveY(y,0)

def convertMove(move):
    print("inside the motor")
    x1 = move.oldPos[0]
    y1 = move.oldPos[1]
    x2 = move.newPos[0]
    y2 = move.newPos[1]
    moveToOldPos(x1,y1)
    moveToNewPos(x1,y1,x2,y2)


def toggleMagnet(state):
    if(state):
        print("Magnet is turned on")
    else:
        print("Magnet is turned off")
