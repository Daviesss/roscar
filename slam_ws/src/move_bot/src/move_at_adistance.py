#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import time
import math

linear_direction = 0.03


class RobotControl():

    def __init__(self):
        rospy.init_node('sample', anonymous=True)
        self.vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.laser_subscriber = rospy.Subscriber('scan', LaserScan, self.laser_callback)
        self.odom_sub = rospy.Subscriber ('/odom', Odometry, self.odom_callback)
        self.cmd = Twist()
        self.laser_msg = LaserScan()
        self.odom_msg = Odometry()
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0
        self.ctrl_c = False
        self.rate = rospy.Rate(10)
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuos publishing systems there is no big deal but in systems that publish only
        once it IS very important.
        """
        while not self.ctrl_c:
            connections = self.vel_publisher.get_num_connections()
    
            if connections > 0:
                self.vel_publisher.publish(self.cmd)
                #rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()

    def shutdownhook(self):
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel()
        #self.ctrl_c = True

    def laser_callback(self, msg):
        self.laser_msg = msg

    def odom_callback(self, msg):
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (self.roll, self.pitch, self.yaw) = euler_from_quaternion (orientation_list)

    def get_front_laser(self):
        time.sleep(1)
        return self.laser_msg.ranges[0]

    def get_laser_full(self):
        time.sleep(1)
        return self.laser_msg.ranges

    def stop_robot(self):
        #rospy.loginfo("shutdown time! Stop the robot")
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel()

    def move_straight(self):

        # Initilize velocities
        self.cmd.linear.x = linear_direction

        # Publish the velocity
        self.publish_once_in_cmd_vel()

    def rotate(self, degrees):
        time.sleep(1)
        target_rad = (degrees * math.pi/180) + self.yaw
        
        if target_rad < (- math.pi):
            target_rad = target_rad + (2 * math.pi)

        if target_rad > (math.pi):
            target_rad = target_rad - (2 * math.pi)
        
        while abs(target_rad - self.yaw) > 0.01:
            self.cmd.angular.z = 0.5 * (target_rad - self.yaw)
            self.vel_publisher.publish(self.cmd)
            self.rate.sleep()
        
        self.stop_robot()


if __name__ == '__main__':
    rospy.init_node('robot_control_node', anonymous=True)
    rc_object = RobotControl()

    while not rc_object.ctrl_c:
        front_laser = rc_object.get_front_laser()
        
        while not front_laser < 0.45:
            rc_object.move_straight()
            front_laser = rc_object.get_front_laser()

        rc_object.stop_robot()
        rc_object.rotate(270)