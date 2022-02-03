
#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist 
import RPi.GPIO as GPIO
import curses
import keyboard


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        if keyboard.is_pressed('w'): #move forward all 4 motors(11,15,31,35)
            GPIO.output(11,True)
            GPIO.output(13,False)
            GPIO.output(15,True)
            GPIO.output(16,False)
            GPIO.output(31,True)
            GPIO.output(33,False)
            GPIO.output(35,True)
            GPIO.output(37,False)
            break

        elif char == ord('s') : #move backword all 4 motors(13,16,33,37)
            GPIO.output(11,False)
            GPIO.output(13,True)
            GPIO.output(15,False)
            GPIO.output(16,True)
            GPIO.output(31,False)
            GPIO.output(33,True)
            GPIO.output(35,False)
            GPIO.output(37,True)

        elif char == ord('a'): #move left(2 motors forward and 2 backward)
            GPIO.output(11,False)
            GPIO.output(13,True)
            GPIO.output(15,True)
            GPIO.output(16,False)
            GPIO.output(31,True)
            GPIO.output(33,False)
            GPIO.output(35,False)
            GPIO.output(37,True)

        elif char == ord('d'): # oposite from left to go right
            GPIO.output(11,True)
            GPIO.output(13,False)
            GPIO.output(15,False)
            GPIO.output(16,True)
            GPIO.output(31,False)
            GPIO.output(33,True)
            GPIO.output(35,True)
            GPIO.output(37,False)


        elif char == 10: # stop all the motors
            GPIO.output(11,False)
            GPIO.output(11,False)
            GPIO.output(15,False)
            GPIO.output(15,False)
            GPIO.output(31,False)
            GPIO.output(31,False)
            GPIO.output(35,False)
            GPIO.output(35,False)

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
