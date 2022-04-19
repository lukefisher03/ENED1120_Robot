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

dBase.gyroTurn(90)
dBase.gyroStraight(100, -2)
wait(2000)
dBase.gyroStraight(100, 4)
dBase.lift("UP")
dBase.gyroStraight(100, -2)
dBase.gyroTurn(-90)
dBase.gyroStraight(600, 24)
dBase.lift("DOWN")
dBase.gyroStraight(600, -5)