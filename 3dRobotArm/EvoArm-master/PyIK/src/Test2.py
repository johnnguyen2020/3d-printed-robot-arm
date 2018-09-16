import serial # import the serial library
import time # import the time library
from time import sleep
#import RPi.GPIO as GPIO
from tkinter import * #import Tkinter GUI library
import random

#Variable declarations
DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
DIR2 = 22
STEP2 = 27
DIR3 = 19
STEP3 = 26

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 180   # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.output(DIR2, CW)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)
GPIO.output(DIR3, CW)



MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
GPIO.output(MODE, RESOLUTION['Full'])


step_count = SPR
delay = .0208 / 1

#defining the functions

#Base motor going CW
def Right():
    GPIO.output(DIR3, CW)
    #print(CW)
    for x in range(1):
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

#Base motor going CCW
def Left():
    GPIO.output(DIR3, CCW)
    #print(CCW)
    for x in range(1):
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

#right motor going clockwise
def Up():
    GPIO.output(DIR, CW)
    #print(CCW)
    for x in range(1):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

#right motor going CCW
def Down():
    GPIO.output(DIR, CCW)
    #print(CCW)
    for x in range(1):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

#Left motor going CCW
def Forward():
    GPIO.output(DIR2, CW)
    print(CCW)
    for x in range(1):
        GPIO.output(STEP2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        sleep(delay)

#Left motor going CW
def Backward():
    GPIO.output(DIR2, CCW)
    print(CCW)
    for x in range(1):
        GPIO.output(STEP2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        sleep(delay)

angle1 = 1
angle2 = 2
angle3 = 3

'''
angle1 = pose.getServoActuator()
angle2 = pose.getServoSwing()
angle3 = pose.getServoElevator()
'''
previous = [1, 1, 1]
result = [0,0,0]


for i in range(500):
    j = random.randint(-100,100)
    k = random.randint(-100,100)
    l = random.randint(-100,100)

    previous_logic = False
    result_lofgic = False
    current = [j, k, l]
    current_logic = False

    for i in range(len(current)):
        result[i] = current[i] - previous[i]
        previous[i] = result[i]

    for i in result:
        if i < 0:
            print("Action CCW")
            #function(int i)
        else:
            print("Action CW")

    print(result)

'''
    def getServoElevator(self):
        print(degrees(self.shoulder_angle))
        return 178.21 - degrees(self.shoulder_angle)

    def getServoActuator(self):
        #print(degrees(self.actuator_angle) + 90)
        return degrees(self.actuator_angle) + 204.78

    def getServoSwing(self):
        #print(degrees(self.swing_angle))
        return 150 - degrees(self.swing_angle)
'''
