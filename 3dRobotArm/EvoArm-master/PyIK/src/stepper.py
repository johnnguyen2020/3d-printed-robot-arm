#cool
import serial # import the serial library
import time # import the time library
from time import sleep
import RPi.GPIO as GPIO
from tkinter import * #import Tkinter GUI library



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


step_count = SPR * 1
delay = .0208 / 1



class StepperActions:
    
    def __init__(self):
        self.logicLeft = False
        self.logicRight = False
        self.logicUp = False
        self.logicDown = False
        self.logicForward = False
        self.logicBackward = False
        self.trigger = 0



##        self.GPIO.setmode(self.GPIO.BCM)
##        self.GPIO.setup(DIR, self.GPIO.OUT)
##        self.GPIO.setup(STEP, self.GPIO.OUT)
##        self.GPIO.output(DIR, CW)
##        self.GPIO.setup(DIR2, self.GPIO.OUT)
##        self.GPIO.setup(STEP2, self.GPIO.OUT)
##        self.GPIO.output(DIR2, CW)
##        self.GPIO.setup(DIR3, self.GPIO.OUT)
##        self.GPIO.setup(STEP3, self.GPIO.OUT)
##        self.GPIO.output(DIR3, CW)
        
    def angle_2_step(self, floatNum):
        self.angle = floatNum
    
    def getKey(item): #wrapper function to sort tuple
        return item[0]
        
#defining the functions
    def movement(self, direction1, direction2, direction3, angle1, angle2, angle3):
        global DIRECTION1
        DIRECTION1 = 0
        global DIRECTION2
        DIRECTION2 = 0
        global DIRECTION3
        DIRECTION3 = 0
        
        if direction1 is "Left":
            DIRECTION1 = CCW
        elif direction1 is "Right":
            DIRECTION1 = CW

        if direction2 is "Down":
            DIRECTION2 = CCW
        elif direction2 is "Up":
            DIRECTION2 = CW

        if direction3 is "Foward":
            DIRECTION3 = CCW
        elif direction3 is "Backward":
            DIRECTION3 = CW

        angleList = [angle1, angle2, angle3]

        stepperDirList = [DIR3, DIR, DIR2]
        stepperList = [STEP3, STEP, STEP2]
        dirList = [DIRECTION1, DIRECTION2, DIRECTION3]
        tupleList = list(zip(angleList, stepperDirList, dirList, stepperList))
        sorted(tupleList, key=lambda item: item[1])
        smallestAngle = 0
        smallestDir = 0
        smallestRotate = 0
        smallStep = 0
        
        midAngle = 0
        midDir = 0
        midRotate = 0
        midStep = 0
        
        bigAngle = 0
        bigDir = 0
        bigRotate = 0
        bigStep = 0
        
#'''this is not how you make tuples'''
##        bigAngle = tuple[2][0]
##        bigDir = tuple[2][1]
##        bigRotate = tuple[2][2]
##        bigStep GPIO.setup(MODE, GPIO.OUT)= tuple[2][3]
##
##        midAngle = tuple[1][0]
##        midDir = tuple[1][1]
##        midRotate = tuple[1][2]
##        midStep = tuple[1][3]
##
##        smallestAngle = tuple[0][0]
##        smallestDir = tuple[0][1]
##        smallestRotate = tuple[0][2]
##        small        myTuple = ([smallestAngle, smallestDir, smallestRotate, smallStep], [midAngle, midDir, midRotate, midStep], [bigAngle, bigDir, bigRotate, bigStep])Step = tuple[0][3]


        myTuple = ([smallestAngle, smallestDir, smallestRotate, smallStep], [midAngle, midDir, midRotate, midStep], [bigAngle, bigDir, bigRotate, bigStep])
        
        GPIO.output(myTuple[0][1], myTuple[0][2])
        for x in range(int(round(myTuple[0][0]/2))):
            GPIO.output((myTuple[0][3], myTuple[1][3], myTuple[2][3]), GPIO.HIGH)
            sleep(delay)
            GPIO.output((myTuple[0][3], myTuple[1][3], myTuple[2][3]), GPIO.LOW)
            sleep(delay)
        
        GPIO.output(myTuple[1][1], myTuple[1][2])
        for x in range(int(round((myTuple[1][0]-myTuple[0][0])/2))):
            GPIO.output((myTuple[1][3], myTuple[2][3]), GPIO.HIGH)
            sleep(delay)
            GPIO.output((myTuple[1][3], myTuple[2][3]), GPIO.LOW)
            sleep(delay)

        GPIO.output(myTuple[2][0], myTuple[2][2])
        for x in range(int(round((bigAngle-myTuple[1][0]-myTuple[0][0])/2))):
            GPIO.output((myTuple[2][3]), GPIO.HIGH)
            sleep(delay)
            GPIO.output((myTuple[2][3]), GPIO.LOW)
            sleep(delay)


        
        '''
        if angle1 > angle 2 and angle 1 > angle3:
            greatestAngle = angle1:
            greatestDir = DIRECTION1
            if angle 2 > angle3
                midAngle = angle2
                midDir = DIRECTION2
                smallestAngle = angle3
                smallestDir = DIRECTION3
            else

        elif angle2 > angle1 and angle2 > angle3
            greatestAngle = angle2:
            greatestDir = DIRECTION2
            if angle 1 > angle3
                midAngle = angle2
                midDir = DIRECTION2
                smallestAngle = angle3
                small        GPIO.output(myTuple[0][1], myTuple[0][2])estDir = DIRECTION3
        '''


    def Right(self, resultnum):
        GPIO.output(DIR3, CW)
        print("CW")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP3, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP3, GPIO.LOW)
            sleep(delay)

    def Left(self, resultnum):
        GPIO.output(DIR3, CCW)
        print("CCW")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP3, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP3, GPIO.LOW)
            sleep(delay)

    def Up(self, resultnum):
        GPIO.output(DIR, CW)
        print("Up")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)

    def Down(self, resultnum):
        GPIO.output(DIR, CCW)
        print("Down")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)

    def Forward(self, resultnum):
        GPIO.output(DIR2, CW)
        print("forward")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP2, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP2, GPIO.LOW)
            sleep(delay)

    def Backward(self, resultnum):
        GPIO.output(DIR2, CCW)
        print("backward")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP2, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP2, GPIO.LOW)
            sleep(delay)
    
