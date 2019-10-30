import RoboPiLib as RPL
import setup
import time
from time import sleep
sensor_pinF = 16
sensor_pinL = 18
sensor_pinR = 17
a = 0
b = 0
def fire():
    for fire in range(0,b):
        RPL.servoWrite(0,1400)
        RPL.servoWrite(1,1600)
        sleep(1)
        RPL.servoWrite(0,1500)
        RPL.servoWrite(1,1500)
        sleep(1)


while True:
    RPL.pinMode(sensor_pinF, RPL.INPUT)
    reading1 = RPL.digitalRead(sensor_pinF)
    RPL.pinMode(sensor_pinL, RPL.INPUT)
    reading2  = RPL.digitalRead(sensor_pinL)
    RPL.pinMode(sensor_pinR, RPL.INPUT)
    reading3 = RPL.digitalRead(sensor_pinR)
    if reading1 == 0:
	b += 1
        a += b	
	fire()
        print("the motor has fired ", a, " times.")
