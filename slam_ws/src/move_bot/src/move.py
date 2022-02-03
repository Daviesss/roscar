#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist
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

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)

# Pins for pulse width modulation on the pi...
pwm_r = GPIO.PWM(ENB,100)
pwm_l = GPIO.PWM(ENA,100)

#Start the dutycycle of the of the pwm. min pulse is 0...
 
pwm_r.start(0)
pwm_l.start(0)

MAX_DUTY_CYCLE = 100 # Max pulse


# screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
# screen.keypad(True)

WHEEL_SEP = 1.2 #distance between you wheels....
velocity_message = Twist()


def move(velocity): 

    linear_speed =velocity.linear.x

    angular_speed = velocity.angular.z
   
    w_l = (2*linear_speed - angular_speed*WHEEL_SEP)/(2.0*WHEEL_SEP);  # left wheel speed
    
    w_r = (2*linear_speed + angular_speed*WHEEL_SEP)/(2.0*WHEEL_SEP);  # right wheel speed

    w_l = abs(int(w_l/0.22)*MAX_DUTY_CYCLE)
    w_r = abs(int(w_r/0.22)*MAX_DUTY_CYCLE)

    print("left wheel speed: ",w_l) 

    print("right wheel speed: ",w_r) 
    

      
# right wheel conditions....

    if w_r < 0:
        pwm_r.ChangeDutyCycle(w_r)
        velocity_message.GPIO.OUTPUT(IN1,False)
        velocity_message.GPIO.OUTPUT(IN2,True)

    if w_r > 0:
        pwm_r.ChangeDutyCycle(w_r)
        velocity_message.GPIO.OUTPUT(IN1,True)
        velocity_message.GPIO.OUTPUT(IN2,False)

    if w_r == 0:
        pwm_r.ChangeDutyCycle(0)
        velocity_message.GPIO.OUTPUT(IN1,True)
        velocity_message.GPIO.OUTPUT(IN2,True)

# left wheel conditions....
            
    if w_l > 0 :
        pwm_l.ChangeDutyCycle(w_l)
        velocity_message.GPIO.OUTPUT(IN3,False)
        velocity_message.GPIO.OUTPUT(IN4,True)

    if w_l < 0 :
        pwm_l.ChangeDutyCycle(w_l)
        velocity_message.GPIO.OUTPUT(IN3,False)
        velocity_message.GPIO.OUTPUT(IN4,True)

    if w_l == 0:
        pwm_l.ChangeDutyCycle(0)
        velocity_message.GPIO.OUTPUT(IN3,True)
        velocity_message.GPIO.OUTPUT(IN4,True)

    
def velcommand():

    rospy.init_node('special_teleop_key_code', anonymous=True)

    rospy.Subscriber("/cmd_vel",Twist, move)

    rospy.spin()  # This keeps Python form exiting until the node is stopped


if __name__ == "__main__":

    try:

        velcommand()

    except rospy.ROSInterruptException:
        rospy.loginfo("The code has terminated")
