import RoboPiLib as RPL
import setup
import time
from time import sleep
sensor_pinM = 4
sensor_pinF = 5
sensor_pinL = 6
sensor_pinR = 7
RPL.pinMode(sensor_pinF, RPL.INPUT)
RPL.pinMode(sensor_pinL, RPL.INPUT)
RPL.pinMode(sensor_pinR, RPL.INPUT)
RPL.pinMode(sensor_pinM, RPL.INPUT)
R = 1
L = 0
while True:
    currentDistanceForward = RPL.analogRead(sensor_pinF)
    currentDistanceLeft = RPL.analogRead(sensor_pinL)
    currentDistanceRight = RPL.analogRead(sensor_pinR)
    currentDistanceSpec = RPL.analogRead(sensor_pinM)
    if currentDistanceLeft >= 50:
        if 350 < currentDistanceLeft < 400:
            RPL.servoWrite(L,1400)
            RPL.servoWrite(R,1600)
        elif currentDistanceLeft <= 350:
            RPL.servoWrite(L,1450)
            RPL.servoWrite(R,1600)
        elif currentDistanceLeft >= 400:
            RPL.servoWrite(L,1400)
            RPL.servoWrite(R,1550)
    elif currentDistanceLeft <= 50:
        if currentDistanceSpec >= 50:
            RPL.servoWrite(L,1400)
            RPL.servoWrite(R,1600)
        elif currentDistanceSpec <= 50:
            RPL.servoWrite(L,1400)
            RPL.servoWrite(R,1550)
