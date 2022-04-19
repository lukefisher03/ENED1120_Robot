from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class GyroBase:
    #constructor function
    def __init__(self,ev3, gyro, l_motor, r_motor, arm, ultrasonic, colorSense):
        self.gyro = gyro
        self.ev3 = ev3
        self.l_motor = l_motor
        self.r_motor = r_motor
        self.arm = arm
        self.ultrasonic = ultrasonic
        self.color = colorSense
    holdingObject = True
    motorConstant = 0.371
    #Move straight
    def gyroStraight(self, runSpeed, dist):
        dist = dist*25.4 #convert to inches

        if self.detectedObject():
            return "Object detected"
        self.r_motor.reset_angle(0)
        self.gyro.reset_angle(0)
        if dist >= 0:
            while self.r_motor.angle() * self.motorConstant <= dist and self.detectedObject() == False:
                self.ev3.screen.print("Distance: " + str(self.r_motor.angle() * self.motorConstant))
                if self.gyro.angle() >= 0 + 1.5:
                    self.r_motor.run(runSpeed)
                    self.l_motor.run(runSpeed-20)
                elif self.gyro.angle() <= 0 - 1.5:
                    self.l_motor.run(runSpeed)
                    self.r_motor.run(runSpeed-20)
                else:
                    self.l_motor.run(runSpeed)
                    self.r_motor.run(runSpeed)
        else:
            while self.r_motor.angle() * self.motorConstant >= dist:#it's not going to run into things moving backwards.
                
                if self.gyro.angle() >= 0 + 1.5:
                    self.r_motor.run(-runSpeed+20)
                    self.l_motor.run(-runSpeed)
                elif self.gyro.angle() <= 0 - 1.5:
                    self.l_motor.run(-runSpeed+20)
                    self.r_motor.run(-runSpeed)
                else:
                    self.l_motor.run(-runSpeed)
                    self.r_motor.run(-runSpeed)
        self.r_motor.hold()
        self.l_motor.hold()#make sure that the motors hold the specific angle at that point.
        wait(500)
        self.l_motor.stop()
        self.r_motor.stop()
        print(dist)
        dist = 0
        return "Successful"
        

    #Turn the robot
    def gyroTurn(self,angle):
        if self.detectedObject():
            return "Object detected"
        self.gyro.reset_angle(0)#Make sure to reset the gyro to 0 to get accurate turns.
        if angle < 0:
            while self.gyro.angle() > angle + 5:
                self.r_motor.run(100)
                self.l_motor.run(-100)
        
        else:
            while self.gyro.angle() < angle - 5:
                self.r_motor.run(-100)
                self.l_motor.run(100)
        self.r_motor.stop()
        self.l_motor.stop()#The angular rotation should not be done with .hold. It creates a jerk in the motors throwing off the values.
        wait(500)
        return "Successful"

    #Lift the arm
    def lift(self, direction):
        self.arm.reset_angle(0)
        if direction == "UP":
            self.arm.run_angle(500, 1500, then=Stop.HOLD, wait=True)
            self.holdingObject = True
        else:
            self.arm.run_angle(500, -1500, then=Stop.HOLD, wait=True)
            self.holdingObject = False
    #Detect objects -> not exactly sure how to distinguish a random object to a package.
    def detectedObject(self):
        if self.holdingObject == False:
            if self.ultrasonic.distance() <= 50:#distance in mm
                return True
            else:
                return False
        else:
            return False #if the arm is holding an object, it should not detect anything.
    def still(self, time_s): #time in seconds
        wait(time_s*1000)
    def identify(self, box):
        self.ev3.screen.clear()
        self.ev3.screen.print("Box: " + str(box))
    
