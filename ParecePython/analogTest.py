import RoboPiLib as RPL
import setup
import time
from time import sleep
sensor_pinF = 0
sensor_pinL = 2
sensor_pinR = 3
RPL.pinMode(sensor_pinF, RPL.INPUT)
RPL.pinMode(sensor_pinL, RPL.INPUT)
RPL.pinMode(sensor_pinR, RPL.INPUT)
R = 1
L = 0


values = []


for i in range(0,100):
   values.append(RPL.analogRead(sensor_pinF))
print(sum(values) / 100)

