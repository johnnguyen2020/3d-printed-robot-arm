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

logicLeft = False
logicRight = False
logicUp = False
logicDown = False
logicForward = False
logicBackward = False
trigger = 0

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 1   # Steps per Revolution (360 / 7.5)


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
def Right():
    GPIO.output(DIR3, CW)
    print(CW)
    for x in range(step_count):
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

def Left():
    GPIO.output(DIR3, CCW)
    print(CCW)
    for x in range(step_count):
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

def Up():
    GPIO.output(DIR, CW)
    print(CCW)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

def Down():
    GPIO.output(DIR, CCW)
    print(CCW)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

def Forward():
    GPIO.output(DIR2, CW)
    print(CCW)
    for x in range(step_count):
        GPIO.output(STEP2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        sleep(delay)

def Backward():
    GPIO.output(DIR2, CCW)
    print(CCW)
    for x in range(step_count):
        GPIO.output(STEP2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        sleep(delay)

def press(*args):
    print('press')
    global pressed
    pressed = True
    appWindow.after(0, loop)

def press_left(*args):
    global logicLeft
    logicLeft = True
    print('leftpress')
    global pressed
    pressed = True
    appWindow.after(0, loop)

def press_right(*args):
    global logicRight
    logicRight = True
    print('rightpress')
    global pressed
    pressed = True
    appWindow.after(0, loop)

def press_up(*args):
    global logicUp
    logicUp = True
    print('uppress')
    global pressed
    pressed = True
    appWindow.after(0, loop)

def press_down(*args):
    global logicDown
    logicDown = True
    print('downpress')
    global pressed
    pressed = True
    appWindow.after(0, loop)

def press_forward(*args):
    global logicForward
    logicForward = True
    print('forwardpress')
    global pressed
    pressed = True
    appWindow.after(0, loop)

def press_backward(*args):
    global logicBackward
    logicBackward = True
    print('backwardpress')
    global pressed
    pressed = True
    appWindow.after(0, loop)

def release(*args):
    print('release')
    global pressed
    pressed = False

    global logicLeft
    logicLeft = False
    global logicRight
    logicRight = False
    global logicUp
    logicUp = False
    global logicDown
    logicDown = False
    global logicForward
    logicForward = False
    global logicBackward
    logicBackward = False

def loop():
    if pressed and logicLeft == True:
        print('loop')
        Left()
        # Infinite loop without delay is bad idea.
        appWindow.after(1, loop)
    if pressed and logicRight == True:
        print('loop')
        Right()
        appWindow.after(1, loop)
    if pressed and logicUp == True:
        print('loop')
        Up()
        appWindow.after(1, loop)
    if pressed and logicDown == True:
        print('loop')
        Down()
        appWindow.after(1, loop)
    if pressed and logicForward == True:
        print('loop')
        Forward()
        appWindow.after(1, loop)
    if pressed and logicBackward == True:
        print('loop')
        Backward()
        appWindow.after(1, loop)

def logic_left():
    global logicLeft
    logicLeft = True
    print('hello')
    global trigger
    trigger = 1

def logic_right():
    logicRight = True

def logic_up():
    logicUp = True

def logic_down():
    logicDown = True

def logic_forward():
    logicForward = True

def logic_backward():
    logicBackward = True

def Stop():
    z = 90

print('Connecting...')

time.sleep(3)
print('Connection established successfully')

appWindow = Tk() # creates the application window (you can use any name)
appWindow.wm_title("GUI CONTROL") #Makes the title that will appear in the top left
appWindow.config(bg = "#828481")


#Control Frame and its contents
controlFrame = Frame(appWindow, width=150, height = 150, bg="#037481", highlightthickness=2, highlightbackground="#111") #defines the control frame
controlFrame.grid() #positions the control frame with the corresponding parameters

btnFrame = Frame(controlFrame, width=150, height = 150, bg="#037481")# defines the button frame with these characteristics
btnFrame.grid() #positions the button frame inside which control buttons will reside

about = "GUI CONTROL"
name = Label(btnFrame, width=12, height=1, text=about, font="bold", justify=CENTER, bg="#037481")
name.grid(row=0, column=2)

upBtn = Button(btnFrame, text="UP", command=Up, bg="green") #defines the UP button
upBtn.bind('<ButtonPress-1>', press_up)
upBtn.bind('<ButtonRelease-1>', release)
upBtn.grid(row=2, column=2, padx=5, pady=5) #positions the UP button within the button frame

downBtn = Button(btnFrame, text="DOWN", command=Down, bg="yellow") #defines the DOWN button
downBtn.bind('<ButtonPress-1>', press_down)
downBtn.bind('<ButtonRelease-1>', release)
downBtn.grid(row=4, column=2, padx=5, pady=5) #positions the UP button within the button frame

leftBtn = Button(btnFrame, text="LEFT", command=Left, bg="orange") #defines the LEFT button
leftBtn.bind('<ButtonPress-1>', press_left)
leftBtn.bind('<ButtonRelease-1>', release)
leftBtn.grid(row=3, column=0, padx=5, pady=5) #positions the LEFT button within the button frame

rightBtn = Button(btnFrame, text="RIGHT", command=Right, bg="blue") #defines the RIGHT button
rightBtn.bind('<ButtonPress-1>', press_right)
rightBtn.bind('<ButtonRelease-1>', release)
rightBtn.grid(row=3, column=3, padx=5, pady=5) #positions the RIGHT button within the button frame


forwardBtn = Button(btnFrame, text="FORWARD", command=Forward, bg="purple") #defines the RIGHT button
forwardBtn.bind('<ButtonPress-1>', press_forward)
forwardBtn.bind('<ButtonRelease-1>', release)
forwardBtn.grid(row=5, column=3, padx=5, pady=5) #positions the RIGHT button within the button frame

backwardBtn = Button(btnFrame, text="BACKWARD", command=Backward, bg="brown") #defines the RIGHT button
backwardBtn.bind('<ButtonPress-1>', press_backward)
backwardBtn.bind('<ButtonRelease-1>', release)
backwardBtn.grid(row=5, column=0, padx=5, pady=5) #positions the RIGHT button within the button frame

stopBtn = Button(btnFrame, text="STOP", command=Stop, bg="red") #defines the STOP button
stopBtn.bind('<ButtonPress-1>', press)
stopBtn.bind('<ButtonRelease-1>', release)
stopBtn.grid(row=3, column=2, padx=5, pady=5) #positions the STOP button within the button frame

appWindow.mainloop()# begins main loop
