#!/usr/bin/env python

import rospy 
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry 
from sensor_msgs.msg import LaserScan



# Now reading the Odometry topic which is Odom..


def 
        take_action(regions)



def take_action(regions):
    msg = Twist()
    linear_x = 0
    angf call_back_laser(msg):
        regions = {
            'right':  min(min(msg.ranges[0:143]), 10),
            'fright': min(min(msg.ranges[144:287]), 10),
            'front':  min(min(msg.ranges[288:431]), 10),
            'fleft':  min(min(msg.ranges[432:575]), 10),
            'left':   min(min(msg.ranges[576:713]), 10),
        }
    ular_z = 0
    
    state_description = ''
    
    if regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] > 1:
        state_description = 'case 1 - nothing'
        linear_x = 0.6
        angular_z = 0
    elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] > 1:
        state_description = 'case 2 - front'
        linear_x = 0.4
        angular_z = 0.3
    elif regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] < 1:
        state_description = 'case 3 - fright'
        linear_x = 0.5
        angular_z = 0.3
    elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] > 1:
        state_description = 'case 4 - fleft'
        linear_x = 0
        angular_z = -0.3
    elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] < 1:
        state_description = 'case 5 - front and fright'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] > 1:
        state_description = 'case 6 - front and fleft'
        linear_x = 0
        angular_z = -0.3
    elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] < 1:
        state_description = 'case 7 - front and fleft and fright'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] < 1:
        state_description = 'case 8 - fleft and fright'
        linear_x = 0.3
        angular_z = 0
    else:
        state_description = 'unknown case'
        rospy.loginfo(regions)



    rospy.loginfo(state_description)
    msg.linear.x = -linear_x
    msg.angular.z = angular_z
    pub.publish(msg)



def move (sped,distance):
    rospy.init_node('merging_odom_and_cmdvel')
    velocity_message = Twist()
    velocity_message.linear = 2
    loop = rospy.Rate (2)
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)

    

    while not rospy.is_shutdown():
        rospy.loginfo('The robot has moved forward')
        pub.publish(velocity_message)



if __name__ == '__main__':
    try :
        sub = rospy.Subscriber('/scan',LaserScan,call_back_laser)
  

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")





