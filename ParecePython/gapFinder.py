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
while True:
    currentDistanceForward = RPL.analogRead(sensor_pinF)
    currentDistanceLeft = RPL.analogRead(sensor_pinL)
    currentDistanceRight = RPL.analogRead(sensor_pinR)
    if currentDistanceLeft >= 315:
        
