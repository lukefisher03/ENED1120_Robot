#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#initalize motor object classes
r_motor = Motor(Port.B)
l_motor = Motor(Port.A)

#initalize the drive train code
drive_train = DriveBase(l_motor, r_motor, wheel_diameter=55.5, axle_track=35)

# Write your program here.
ev3.speaker.beep()

drive_train.straight(1000)
