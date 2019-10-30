import RoboPiLib as RPL
import setup
import time
from time import sleep  
sensor_pinF = 16
sensor_pinL = 18
sensor_pinR = 17

def move_forward():
    while True: 
        RPL.pinMode(sensor_pinF, RPL.INPUT)
        reading1 = RPL.digitalRead(sensor_pinF)  
        RPL.pinMode(sensor_pinL, RPL.INPUT)
        reading2  = RPL.digitalRead(sensor_pinL)
        RPL.pinMode(sensor_pinR, RPL.INPUT)
        reading3 = RPL.digitalRead(sensor_pinR) 
        if reading1 ==1 or reading2==1 and reading3 == 1: 
            RPL.servoWrite(0,1450)
            RPL.servoWrite(1,1550)
        elif reading2 == 0 and reading3 == 0:
            RPL.servoWrite(0,1600)
            RPL.servoWrite(1,1400)
	elif reading2 == 0:
            RPL.servoWrite(0,1400)
            RPL.servoWrite(1,1550)
        elif reading3 == 0:
            RPL.servoWrite(0,1450)
            RPL.servoWrite(1,1600)
	else:
            RPL.servoWrite(0,1500)
            RPL.servoWrite(1,1500)


move_forward()
