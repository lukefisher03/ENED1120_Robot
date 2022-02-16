#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time




# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#initalize motor object classes
r_motor = Motor(Port.D)
l_motor = Motor(Port.C)
gyro = GyroSensor(Port.S4)

def gyroStraight(dist):
    r_motor.reset_angle(0)
    gyro.reset_angle(0)
    if dist >= 0:
        
        while r_motor.angle() * 0.60 <= dist:
            ev3.screen.print(gyro.angle())
            print(r_motor.angle())
            
            if gyro.angle() >= 0 + 1.5:
                r_motor.run(300)
                l_motor.run(250)
            elif gyro.angle() <= 0 - 1.5:
                l_motor.run(300)
                r_motor.run(250)
            else:
                l_motor.run(300)
                r_motor.run(300)
    else:
        while r_motor.angle() * 0.60 >= dist:
            ev3.screen.print(gyro.angle())
            print(r_motor.angle())
            
            if gyro.angle() >= 0 + 1.5:
                r_motor.run(-250)
                l_motor.run(-300)
            elif gyro.angle() <= 0 - 1.5:
                l_motor.run(-250)
                r_motor.run(-300)
            else:
                l_motor.run(-300)
                r_motor.run(-300)

    r_motor.hold()
    l_motor.hold()#make sure that the motors hold the specific angle at that point.
    wait(500)
    l_motor.stop()
    r_motor.stop()
    
def gyroTurn(angle):
    gyro.reset_angle(0)#Make sure to reset the gyro to 0 to get accurate turns.
    if angle < 0:
        while gyro.angle() > angle + 4:
            ev3.screen.print(gyro.angle())
            r_motor.run(70)
            l_motor.run(-70)
    
    else:
        while gyro.angle() < angle - 4:
            ev3.screen.print(gyro.angle())
            r_motor.run(-70)
            l_motor.run(70)

    r_motor.stop()
    l_motor.stop()#The angular rotation should not be done with .hold. It creates a jerk in the motors throwing off the values.
    wait(500)



gyroStraight(1200)
gyroStraight(-1200)


gyroStraight(1200)
gyroStraight(-1200)

gyroStraight(1200)
gyroStraight(-1200)


#initalize the drive train code

# Write your program here.

ev3.speaker.beep()

