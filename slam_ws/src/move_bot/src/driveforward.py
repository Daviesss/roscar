#!/usr/bin/env python


from geometry_msgs import msg
import rospy 
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
import math 
import time

#Setting all coordinate to 0..
x = 0
y = 0
yaw = 0 
pose_topic_name = '/tutrle1/pose'
cmd_topic = '/cmd_vel'





def angle (speed,distance) :
    velocity_message = Twist ()
    x0 =x =0
    y0 =y = 0
    z0 =z = 2
    velocity_message.angular.z = speed
    distance_moved = 2.0
    loop_rate = rospy.Rate(20) # publishing the velocity at 10 Hz (20 times a second)
    cmd_vel_topic = '/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)


def rotate (angular_speed_degree,relative_angle_degree,clockwise) :
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    # velocity_message.linear.z = 0 not nedded since its in 2d ..
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0
    angular_speed = math.radians(abs(angular_speed_degree))

    if (clockwise) :
        velocity_message.angular.z = -abs(angular_speed)
    else :
        velocity_message.angular.z = abs(angular_speed)

    
    angle_moved = 0.0
    loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
    cmd_vel_topic='/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo("car rotates")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()

        print ('current_angle_degree: ',current_angle_degree)
                       
        if  (current_angle_degree>relative_angle_degree):
            rospy.loginfo("reached")
            break

    #finally, stop the robot when the distance is moved
        velocity_message.angular.z =0
        velocity_publisher.publish(velocity_message)




# def move_left (speed,distance) :
#     velocity_message = Twist()
#     x0 =x = 0
#     y0 =y=  0
#     z0 =z = 2
#     velocity_message.angular.z = speed
#     distance_moved = 2
#     loop = rospy.Rate(20)
#     rospy.loginfo("The car is moving at an angle")
#     rospy_pub = rospy.Publisher(cmd_topic,Twist,queue_size=10)
#     while True:
#         rospy.loginfo("The car starts to move at an angle")
#         rospy_pub.publish(velocity_message)

# def move_backward(speed,distance):
#     velocity_message = Twist()
#     #set the initial position of the robot 
#     x0 = x = -2
#     y0 = y = 0
#     # z0 = 0
#     velocity_message.linear.x = -2
#     distance_moved = 0
#     rospy.loginfo("Now the robot is moving backward")
#     rospy.init_node("drive_forward")
#     velocity_pub = rospy.Publisher(cmd_topic,Twist,queue_size=1)


#     while True :
#         rospy.loginfo("Now the robot is driving ..lol,i mean moving backward")
#         velocity_pub.publish(velocity_message)
#         # rospy.spin()

def move_forward (speed,distance):
    velocity_message = Twist()
    #Getting the initial state of the robot ..
    x0 =x
    y0 =y 
    # z0 = z  not really needed since its a cartisian cordinate frame 2D..
    velocity_message.linear.x=speed 
    distance_moved = 0
    # loop = rospy.Rate(10) #The rate speeed at which the cmd_vel is publishing..
    # loop = rospy.Rate(2)

    rospy.loginfo("Now the robot is moving")
    rospy.init_node("drive_forward")
    velocity_pub = rospy.Publisher(cmd_topic,Twist,move_forward,queue_size=1)


    while True :
       rospy.loginfo("Now we get the car to move forward")
       velocity_pub.publish(velocity_message)
    #    rospy.spin(0)
    #    break
  


#creating a function that shows the pose of the robot on motion ..

def call_back (pose_message) :
    x = pose_message.x
    y = pose_message.y
    z = pose_message.z 
    # rospy_sub.publish(pose_message)


rospy.loginfo("getting pose of the robot in motion and also in static state")
rospy_sub = rospy.Subscriber(pose_topic_name,Pose,call_back)
    # rospy_sub.publish(pose_message)


if __name__ == '__main__':
    # try:
        # # move_forward(1.0,5.0)
        # rotate (90,90,True)
        angle(1.0,5.0)
    
        
      
    # except rospy.ROSInterruptException:
    #     rospy.loginfo("node terminated.")
#!/usr/bin/env python


from geometry_msgs import msg
import rospy 
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
import math 
import time

#Setting all coordinate to 0..
x = 0
y = 0
yaw = 0 
pose_topic_name = '/tutrle1/pose'
cmd_topic = '/cmd_vel'





def angle (speed,distance) :
    velocity_message = Twist ()
    x0 =x =0
    y0 =y = 0
    z0 =z = 2
    velocity_message.angular.z = speed
    distance_moved = 2.0
    loop_rate = rospy.Rate(20) # publishing the velocity at 10 Hz (20 times a second)
    cmd_vel_topic = '/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)


def rotate (angular_speed_degree,relative_angle_degree,clockwise) :
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    # velocity_message.linear.z = 0 not nedded since its in 2d ..
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0
    angular_speed = math.radians(abs(angular_speed_degree))

    if (clockwise) :
        velocity_message.angular.z = -abs(angular_speed)
    else :
        velocity_message.angular.z = abs(angular_speed)

    
    angle_moved = 0.0
    loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
    cmd_vel_topic='/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo("car rotates")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()

        print ('current_angle_degree: ',current_angle_degree)
                       
        if  (current_angle_degree>relative_angle_degree):
            rospy.loginfo("reached")
            break

    #finally, stop the robot when the distance is moved
        velocity_message.angular.z =0
        velocity_publisher.publish(velocity_message)




# def move_left (speed,distance) :
#     velocity_message = Twist()
#     x0 =x = 0
#     y0 =y=  0
#     z0 =z = 2
#     velocity_message.angular.z = speed
#     distance_moved = 2
#     loop = rospy.Rate(20)
#     rospy.loginfo("The car is moving at an angle")
#     rospy_pub = rospy.Publisher(cmd_topic,Twist,queue_size=10)
#     while True:
#         rospy.loginfo("The car starts to move at an angle")
#         rospy_pub.publish(velocity_message)

# def move_backward(speed,distance):
#     velocity_message = Twist()
#     #set the initial position of the robot 
#     x0 = x = -2
#     y0 = y = 0
#     # z0 = 0
#     velocity_message.linear.x = -2
#     distance_moved = 0
#     rospy.loginfo("Now the robot is moving backward")
#     rospy.init_node("drive_forward")
#     velocity_pub = rospy.Publisher(cmd_topic,Twist,queue_size=1)


#     while True :
#         rospy.loginfo("Now the robot is driving ..lol,i mean moving backward")
#         velocity_pub.publish(velocity_message)
#         # rospy.spin()

def move_forward (speed,distance):
    velocity_message = Twist()
    #Getting the initial state of the robot ..
    x0 =x
    y0 =y 
    # z0 = z  not really needed since its a cartisian cordinate frame 2D..
    velocity_message.linear.x=speed 
    distance_moved = 0
    # loop = rospy.Rate(10) #The rate speeed at which the cmd_vel is publishing..
    # loop = rospy.Rate(2)

    rospy.loginfo("Now the robot is moving")
    rospy.init_node("drive_forward")
    velocity_pub = rospy.Publisher(cmd_topic,Twist,move_forward,queue_size=1)


    while True :
       rospy.loginfo("Now we get the car to move forward")
       velocity_pub.publish(velocity_message)
    #    rospy.spin(0)
    #    break
  


#creating a function that shows the pose of the robot on motion ..

def call_back (pose_message) :
    x = pose_message.x
    y = pose_message.y
    z = pose_message.z 
    # rospy_sub.publish(pose_message)


rospy.loginfo("getting pose of the robot in motion and also in static state")
rospy_sub = rospy.Subscriber(pose_topic_name,Pose,call_back)
    # rospy_sub.publish(pose_message)


if __name__ == '__main__':
    # try:
        # # move_forward(1.0,5.0)
        # rotate (90,90,True)
        angle(1.0,5.0)
    
        
      
    # except rospy.ROSInterruptException:
    #     rospy.loginfo("node terminated.")
