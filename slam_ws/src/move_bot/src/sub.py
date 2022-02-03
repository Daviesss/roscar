#!/usr/bin/env python
import rospy 
from nav_msgs.msg import Odometry

def call_back (msg) :
    print (msg.pose)


rospy.init_node('sub')
sub = rospy.Subscriber('/odom',Odometry,call_back)
loop = rospy.Rate(10)
rospy.loginfo("Getting information from the robot on its position")


