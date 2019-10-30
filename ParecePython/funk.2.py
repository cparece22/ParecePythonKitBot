import RoboPiLib as RPL
import setup
import time
from time import sleep
from funk1 import moveFor
sensor_pinF = 16
sensor_pinL = 18
sensor_pinR = 17
RPL.pinMode(sensor_pinF, RPL.INPUT)
RPL.pinMode(sensor_pinL, RPL.INPUT)
RPL.pinMode(sensor_pinR, RPL.INPUT)
R = 1
L = 0
x = 0
while True:
    reading1 = RPL.digitalRead(sensor_pinF)
    reading2  = RPL.digitalRead(sensor_pinL)
    reading3 = RPL.digitalRead(sensor_pinR)
    if reading1 == 0:
        x += 1
        moveFor(x)

