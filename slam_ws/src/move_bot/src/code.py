#!/usr/bin/env python
import curses
import rospy 
from geometry_msgs.msg import Twist
import time
import RPi.GPIO as GPIO


#Declearing all the pins...
ENA = 12
IN1 = 13
IN2 = 15
IN3 = 16
IN4 = 19
ENB = 18
SPEED = 150
STOP = 0
wheel_seperation = 4.75
wheel_rad = 2.34

rospy.init_node('code',anonymous=True) #initilizing the node ....
velocity_message = Twist() #saving the Twist message into a variable called Velocity_message..
publish_command_velocity = rospy.Publisher('/cmd_vel',Twist,queue_size=1) #Publishing to the command velocity topic which is "/cmd_vel"
loop_rate = rospy.Rate(2)


def message_call():
    angular_speed = velocity_message.angular.z #Twist message values from cmd_vel..
    linear_speed  = velocity_message.linear.y  #Twist message values from cmd_vel..

    left_wheel = (2*angular_speed -linear_speed*wheel_seperation)/(2.0*wheel_rad)
    right_wheel = (2*linear_speed +angular_speed*wheel_seperation)/(2.0*wheel_rad)

    



GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


while True :
    char = screen.getch()
    if char == ord ("q"):
        break #once the key is pressed the code stops executing and closes....
    if message_call()> 0:
         #Vehicle moves forward....
        velocity_message.GPIO.OUTPUT(ENA,SPEED)
        velocity_message.GPIO.OUTPUT(IN1,False)
        velocity_message.GPIO.OUTPUT(IN2,True)
        velocity_message.GPIO.OUTPUT(IN3,False)
        velocity_message.GPIO.OUTPUT(IN4,True)
        velocity_message.GPIO.OUTPUT(ENB,SPEED)
        break 
        
    elif char == ord ('x'):
        #Vehicle moves backward....
        velocity_message.GPIO.OUTPUT(ENA,SPEED)
        velocity_message.GPIO.OUTPUT(IN1,True)
        velocity_message.GPIO.OUTPUT(IN2,False)
        velocity_message.GPIO.OUTPUT(IN3,True)
        velocity_message.GPIO.OUTPUT(IN4,False)
            
    elif char == ord ('a'):
        #Vehicle moves Right.....
        velocity_message.GPIO.OUTPUT(ENA,SPEED)
        velocity_message.GPIO.OUTPUT(IN1,True)
        velocity_message.GPIO.OUTPUT(IN2,False)
        velocity_message.GPIO.OUTPUT(IN3,False)
        velocity_message.GPIO.OUTPUT(IN4,True)

    elif char == ord ('d'):
        #Vehicle moves left......
        velocity_message.GPIO.OUTPUT(ENA,SPEED)
        velocity_message.GPIO.OUTPUT(IN1,False)
        velocity_message.GPIO.OUTPUT(IN2,True)
        velocity_message.GPIO.OUTPUT(IN3,True)
        velocity_message.GPIO.OUTPUT(IN4,False)

    elif char == 10 :
        #Vehicle stops ....
        velocity_message.GPIO.OUTPUT(ENA,STOP)
        velocity_message.GPIO.OUTPUT(IN1,STOP)
        velocity_message.GPIO.OUTPUT(IN2,STOP)
        velocity_message.GPIO.OUTPUT(IN3,STOP)
        velocity_message.GPIO.OUTPUT(IN4,STOP)
        velocity_message.GPIO.OUTPUT(ENB,STOP)

    while not rospy.is_shutdown():
        rospy.loginfo("The robot now publish to the command velocity topic")
        publish_command_velocity.publish(velocity_message)
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        GPIO.cleanup()


        


    







