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

    if currentDistanceForward >= 315:
        RPL.servoWrite(L,1500)
        RPL.servoWrite(R,1500)
    elif 300 < currentDistanceLeft < 400:
        RPL.servoWrite(L,1400)
        RPL.servoWrite(R,1600)
    elif currentDistanceLeft <= 300:
        RPL.servoWrite(L,1450)
        RPL.servoWrite(R,1600)
    elif currentDistanceLeft >= 400:
        RPL.servoWrite(L,1400)
        RPL.servoWrite(R,1550)

