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

def moveFor(pulses):
    
    for pulse in range(0,pulses):
        RPL.servoWrite(R, 1600)
        RPL.servoWrite(L, 1400)
        sleep(1)
        RPL.servoWrite(R, 1500)
        RPL.servoWrite(L, 1500)
        sleep(1)

