#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist 

def move_accordingly (speed,distance,clockwise):
    rospy.init_node('nake_robotmoveright',anonymous=True)
    velocity_message = Twist () #saving the twist message into a variable called velocity_message...
    # when the robot is at initial state ....
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1) #publishing to the topic called cmd_vel
    loop = rospy.Rate(10)
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.angular.x = 0
    velocity_message.angular.z = 0

    # The robot moves forward ....
    velocity_message.linear.x = abs (speed) #with a speed of 1.0 metre per seconds....
    if distance == 5 :
        velocity_message.linear.x = 0

    if clockwise < 0:
        speed +=0.1
        velocity_message.angular.z = abs(speed)

    else :
        speed -=0.1
        velocity_message.angular.z = - abs (speed)
        velocity_message.linear.x = 0


        return distance 
    

    while not rospy.is_shutdown():
        rospy.loginfo("The node is being published to command velocity")
        pub.publish(velocity_message)
        rospy.spin()


if __name__ == '__main__':
    try:
       move_accordingly(1.0,5.0,True)

    except rospy.ROSInterruptException:
        rospy.loginfo("The code has terminated")





