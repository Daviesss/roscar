#!/usr/bin/env python
import rospy 
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped


velocity_message = Twist()
rospy.init_node('odom_sub', anonymous=True)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)

initpose_msg = PoseWithCovarianceStamped()
initpose_msg.pose.pose.position.x = 0.0
initpose_msg.pose.pose.position.y = 0.0
initpose_msg.pose.pose.position.z = 0.0


velocity_message.linear.x = 2

# Pub = rospy.Publisher('/initialpose',PoseWithCovarianceStamped,queue_size=1)
# Pub.publish(initpose_msg)


def move (speed,distance):

   if initpose_msg.pose.pose.position.x > 0.0:
     rospy.loginfo("The robot moves forward")
    #  pub.publish(velocity_message)
     velocity_message.angular.z = 2


while rospy.is_shutdown():
    rospy.init_node('odom_sub',anonymous=True)
    pub.publish(velocity_message)

    # Pub = rospy.Publisher('/initialpose',PoseWithCovarianceStamped,queue_size=1)
    # Pub.publish(initpose_msg)
    # rospy.spin()


def main ():
    Pub = rospy.Publisher('/initialpose',PoseWithCovarianceStamped,queue_size=1)
    Pub.publish(initpose_msg)




if __name__ == '__main__':
    try :

        # Pub = rospy.Publisher('/initialpose',PoseWithCovarianceStamped,queue_size=1)
        move (1.0,5.0)



        
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")






    