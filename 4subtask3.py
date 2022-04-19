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

dBase.gyroStraight(600,16)
ev3.screen.print("Identifying...")
dBase.gyroStraight(100,-0.5)
ev3.speaker.beep()
dBase.gyroStraight(100,-0.5)
ev3.speaker.beep()
dBase.gyroStraight(100,-0.5)
ev3.speaker.beep()
dBase.identify(4)
wait(15000)
ev3.speaker.beep()