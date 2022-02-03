#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from move_robot import MoveRobot 

class stopwall():
    def __init__(self):

        self.sub = sub = rospy.Publisher('/scan',LaserScan,self.callback)
        self.moverobot_object= MoveRobot()
        
    def callback(self,msg):

        if msg.ranges[0] > 1:
            linear_x =  0.5 
            angular_z = 0.0 
            self.moverobot_object.send_cmd(linear_x,angular_z)

        #if the distance to an obstacle in front of the bot is smaller 