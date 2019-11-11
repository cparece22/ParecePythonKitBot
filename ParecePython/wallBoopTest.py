import RoboPiLib as RPL
import setup
import time
from time import sleep
sensor_pinF = 5
sensor_pinL = 6
sensor_pinR = 7
RPL.pinMode(sensor_pinF, RPL.INPUT)
RPL.pinMode(sensor_pinL, RPL.INPUT)
RPL.pinMode(sensor_pinR, RPL.INPUT)
R = 1
L = 0
startDistanceLeft = RPL.analogRead(sensor_pinL)
startDistanceRight = RPL.analogRead(sensor_pinR)
startDistanceForward = RPL.analogRead(sensor_pinF)

while True:
    currentDistanceForward = RPL.analogRead(sensor_pinF)
    currentDistanceLeft = RPL.analogRead(sensor_pinL)
    currentDistanceRight = RPL.analogRead(sensor_pinR)
#1.2
    if 308 <= currentDistanceForward <= 310:
        RPL.servoWrite(L,0)
        RPL.servoWrite(R,0)
        print("Optimal Distance Achieved")
        sleep(1)
        print("Commence Wall Boop")
        RPL.servoWrite(L,1400)
        RPL.servoWrite(R,1600)
        sleep(2.00)
        RPL.servoWrite(L,0)
        RPL.servoWrite(R,0) 
        break
    elif currentDistanceForward <= 310:
        RPL.servoWrite(L,1400)
        RPL.servoWrite(R,1600)
    elif currentDistanceForward >= 310:
        RPL.servoWrite(L,1600)
        RPL.servoWrite(R,1400)

