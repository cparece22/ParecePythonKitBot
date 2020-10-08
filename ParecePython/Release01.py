import RoboPiLib as RPL
import setup
from time import sleep
import sys
import argv

inputList = sys.argv[1:]

R = 1
L = 0
for input in inputList:
    if input == "W":
        RPL.servoWrite(L,1600 )
        RPL.servoWrite(R.1400 )
    elif input == "S":
        RPL.servoWrite(L,1400)
        RPL.servoWrite(R,1600)
    elif input == "A":
        RPL.servoWrite(L,1500)
        RPL.servoWrite(R,1600)
    elif input == "D":
        RPL.servoWrite(L,1400)
        RPL.servoWrite(R,1500)
    else:
        RPL.servoWrite(L,0)
        RPL.servoWrite(R,0)
    sleep(.5)
    RPL.servoWrite(L,1500)
    RPL.servoWrite(R,1500)
