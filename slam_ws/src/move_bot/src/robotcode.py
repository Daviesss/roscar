#!/usr/bin/env python   
import rospy 
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan
import time

#Setting the initial position of linear velocity of the x,y and z coordinate to 0....
x = 0
y = 0 
z = 0

# Given that all coordinates are set to 0.....


#Laser scan callback function for object...


def call_back_laser(msg):
    regions = [
        min(min(msg.ranges[0:143]), 10),
        min(min(msg.ranges[144:287]), 10),
        min(min(msg.ranges[288:431]), 10),
        min(min(msg.ranges[432:575]), 10),
        min(min(msg.ranges[576:713]), 10),
    ]
    rospy.loginfo(regions)

def main():
    rospy.init_node('robotcode')

    sub = rospy.Subscriber('/scan', LaserScan, call_back_laser)

    rospy.spin()
        
                
##############################################################################################

def turn_left (speed,distance):   
    rospy.init_node('robotcode',anonymous=True)
    velocity_message = Twist ()
    velocity_message.angular.z = -2 
    distance_moved = 0
    loop = rospy.Rate (10)
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)

        


    while not rospy.is_shutdown():
        rospy.loginfo("The robot starts moving left")
        pub.publish(velocity_message)
        

def turn_right (speed,distance):
    rospy.init_node('robotcode',anonymous=True)
    velocity_message = Twist ()
    velocity_message.angular.z = 2
    distance_moved = 0
    loop =rospy.Rate (10)
    pub =rospy.Publisher('/cmd_vel',Twist,queue_size=1)

    while not rospy.is_shutdown():
        rospy.loginfo('The robot starts turning right')
        pub.publish(velocity_message)



def move_Forward (speed,distance):
    
    x0 = x
    y0 = y 
    z0 = z
    rospy.init_node('robotcode',anonymous=True)
    velocity_message = Twist ()
    velocity_message.linear.x = speed
    distance_moved = 0
    loop =rospy.Rate(10)
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    

    while not rospy.is_shutdown():
       rospy.loginfo("The car is moving Forward")
       pub.publish(velocity_message)

#######################################################################################################   
def stop (speed,distance):
    # velocity_message = Twist ()
    x0 = x = 0
    y0 = y = 0
    z0 =z =  0
    rospy.init_node('robotcode',anonymous=True)
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0
    distance_moved = 0
    loop = rospy.Rate(10)
    pub = rospy.Publisher('cmd_vel',Twist,queue_size=1)
    

    while not rospy.is_shutdown() :
        rospy.loginfo('The robot has stopped')
        pub.publish(velocity_message)
    



if __name__ == '__main__' :
    try :
        turn_left(1.0,5.0)
        # rospy.Duration(20)
        # stop(0.0,0.0)

       

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
