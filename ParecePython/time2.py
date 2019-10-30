import RoboPiLib as RPL
import setup
import time
from time import sleep
sensor_pinF = 16
sensor_pinL = 18
sensor_pinR = 17
RPL.pinMode(sensor_pinF, RPL.INPUT)
RPL.pinMode(sensor_pinL, RPL.INPUT)
RPL.pinMode(sensor_pinR, RPL.INPUT)
R = 1
L = 0
def leftTimer():
    global timeL
    timeL = time.time()
def rightTimer():
    global timeR  
    timeR = time.time()
def leftGo():
    RPL.servoWrite(L,1400)
def rightGo():
    RPL.servoWrite(R,1600)
def leftStop():
    RPL.servoWrite(L,1500)
def rightStop():
    RPL.servoWrite(R,1500)
leftTimer()
rightTimer()
def GoTime(): 
    leftTimer()
    rightTimer()
    while True:
        time.sleep(0.05)
        timePastL = time.time() - timeL
        timePastR = time.time() - timeR
        if timePastL <= 2:
            leftGo()
        elif timePastL >= 2:
            leftStop()
        if timePastR <= 3:
            rightGo()
        elif timePastR >= 3:
            rightStop()
GoTime()
