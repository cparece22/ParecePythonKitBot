import RoboPiLib as RPL
import setup
import time
from time import sleep
sensor_pinF = 0
sensor_pinL = 1
sensor_pinR = 0
RPL.pinMode(sensor_pinF, RPL.INPUT)
RPL.pinMode(sensor_pinL, RPL.INPUT)
RPL.pinMode(sensor_pinR, RPL.INPUT)
R = 1
L = 0

while True:
    a = RPL.analogRead(sensor_pinF)
    if a < 315:
        RPL.servoWrite(L,1400)
        RPL.servoWrite(R,1600)
    elif 315 < a < 570:
        RPL.servoWrite(L,1450)
        RPL.servoWrite(R,1550)
    else:
        RPL.servoWrite(L,1500)
        RPL.servoWrite(R,1500)

