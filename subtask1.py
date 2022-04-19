#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from GyroBase import GyroBase
# Create your objects here.
ev3 = EV3Brick()

#initalize motor object classes
l_motor = Motor(Port.A)
r_motor = Motor(Port.B)
arm = Motor(Port.D)
gyro = GyroSensor(Port.S3)
ultrasonic = UltrasonicSensor(Port.S2)
colorSense = ColorSensor(Port.S4)

dBase = GyroBase(ev3, gyro, l_motor,r_motor,arm,ultrasonic,colorSense)

stopDist = 36
        
dBase.gyroStraight(600, 60)
dBase.gyroTurn(90)
dBase.gyroStraight(600,30) 
dBase.gyroTurn(-90)
dBase.gyroStraight(600,5)
dBase.lift("UP")
dBase.gyroTurn(90)
dBase.gyroStraight(600,12)
dBase.gyroTurn(-90)
dBase.gyroStraight(600,30)
dBase.gyroTurn(-90)
dBase.gyroStraight(600,36)
dBase.gyroTurn(90)
dBase.gyroStraight(600,10)
dBase.lift("DOWN")