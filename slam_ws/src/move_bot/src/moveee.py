#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time 
import math 
from std_srvs.srv import Empty

def move (speed,distance): #Robot moves forward.....
    # rospy.init_node('moveee',anonymous=True)
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    velocity_message= Twist()
    linear_speed =velocity_message.linear.x
    distance_moved = 0.0 
    loop_rate = rospy.Rate(10)
    t0 = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo("The robot moves forward")
        loop_rate.sleep()
        t1 = rospy.Time.now().to_sec()
        # distance_moved = (t1-t0) * speed
        # print  (distance_moved) 
        pub.publish(linear_speed)

def rotate(angular_speed_degree,relative_angle_degree,clockwise):
    velocity_message = Twist() #Storing the twist message into a variable called velocity_message...
    #For linear velocity...
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    #For angular velocity....
    velocity_message.angular.x =0
    velocity_message.angular.y =0
    velocity_message.angular.z =0

    # angular_speed = math.radians(abs(angular_speed_degree))
    angular_speed = velocity_message.angular.z

    if (clockwise):
        velocity_message.angular.z = -abs(angular_speed)
    else :
        velocity_message.angular.z =  abs(angular_speed)
    
    # angle_moved = 0.0
    loop_rate = rospy.Rate(10)
    command_velocity = '/cmd_vel'
    velocity_pub =rospy.Publisher(command_velocity,Twist,queue_size=10)

    t0 = rospy.Time.now()
    while True :
        rospy.loginfo("The robot rotates")
        velocity_pub.publish(velocity_message)
        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0) * angular_speed_degree
        loop_rate.sleep()
        print('current_angle_degree:',current_angle_degree)
        
        if (current_angle_degree > relative_angle_degree):
            rospy.loginfo("reached")
            break

        velocity_pub.publish(angular_speed)


if __name__ == '__main__':
    try:
        rospy.init_node('moveee',anonymous=True)
        move(0.3,5.0)
        time.sleep()
        rotate (90,90,True)

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")




        
    