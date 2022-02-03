#!/usr/bin/env python
import rospy 

from sensor_msgs.msg import LaserScan



rc = LaserScan()


laser1 = rc.get_laser(360)


print ("The distance measured is :", laser1)
