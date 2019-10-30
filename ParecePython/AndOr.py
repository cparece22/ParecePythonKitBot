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
x = 0
while True:
    reading1 = RPL.digitalRead(sensor_pinF)
    reading2 = RPL.digitalRead(sensor_pinR)
    reading3 = RPL.digitalRead(sensor_pinL)
    print(reading2, reading3) 
    if reading2 == 0 and reading3 == 0:
        RPL.servoWrite(L,1600 )
        RPL.servoWrite(R,1400 )
        x += 1
    elif reading1 == 0 or  x >= 5:
        RPL.servoWrite(L,1500)
        RPL.servoWrite(R,1500)





