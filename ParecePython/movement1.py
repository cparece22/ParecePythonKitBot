import RoboPiLib as RPL
import setup
import time
from time import sleep
def moveForward(): 
    RPL.servoWrite(0,1400)
    RPL.servoWrite(1,1600)
    time.sleep(3)
    RPL.servoWrite(0,1500)
    RPL.servoWrite(1,1500)
moveForward()
