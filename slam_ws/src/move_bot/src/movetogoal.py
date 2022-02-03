#!/usr/bin/env python

#import ros libaries.....
from os import stat_result
import rospy 
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from tf import transformations
import math 



#Robot state Variables.......
position = Point()
yaw = 0
#machine state of the robot......
state = 0


#Goal ..
desired_position = Point()
desired_positionx =  5
desired_positiony =  8
desired_positionz =  0
position.y 
position.x 


#parameters ....
yaw_precision = math.pi / 90 
dist_position = 0.3 


#defining a publisher variable ....
pub = None 

#function for the  position from the odometry...
def clbk_odom(msg) :
    global position
    global yaw

    position = msg.pose.pose.position 

    quaternion = (
        msg.pose.pose.orientation.x,
        msg.pose.pose.orientation.y,
        msg.pose.pose.orientation.z,
        msg.pose.pose.orientation.w
    )
    eurler = transformations.euler_from_quaternion(quaternion)
    #roll = eurler [0]
    #pitch = eurler[1]
    yaw = eurler[2]

#Defining  the change state function...
def change_state(state) :
    global state 
    state = state 
    print ('state changed to [%5]' % state)

def fix_yaw(des_pos):
    global yaw, pub , yaw_precision,state
    desired_yaw = math.atan2(des_pos.y - position.y, des_pos.x - position.x)
    err_yaw = desired_yaw - yaw

    twist_msg = Twist ()
    if math.fabs(err_yaw) > yaw_precision :
        twist_msg.angular.z = 0.7 if err_yaw >  0 else -0.7
    
    pub.publish(twist_msg)

    #state change conditions ...


    if math.fabs(err_yaw)  <= yaw_precision:
        print ('yaw error : [%5] ') & err_yaw
        change_state(1)
        


def main():
    global pub 

    rospy.init_node('gotopoint')

    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)

    #sub_laser = rospy.Subscriber('/scan',LaserScan, clbk_laser)
    sub_odom  = rospy.Subscriber('/odom',Odometry,clbk_odom)

    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        if state == 0:
            fix_yaw(desired_position)
        else:
            rospy.logerr('unknown state!')
            pass 
        rate.sleep()





if __name__ == '__main__' :
    main() 












