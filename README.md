# roscar
A mobile robot powered by ros .
I was able to  map my living room with a 2D ydlidar ...

A Differential-Drive Mobile Robot...

In this project, I built a differential-drive mobile robot, using the ROS framework, for SLAM(Simultaneous localization and mapping). The map was built using lidar scans. I implemented an Extended Kalman Filter for state estimation that fused lidar data with wheel odometry(Wheel Encoder).

ROS nodes are in Python with one C++ Rosserial node (on the Arduino).


C++ rosserial node for low-level control of the motors an![slam2](https://user-images.githubusercontent.com/97457075/160631298-def3c188-043f-4252-97ed-8e5232396b9c.jpg)
d measurement of wheel speeds.

LAUNCH FILES:
 Lidar_view.launch: Starts the node for publishing lidar scan data.
 
PROCEDURE FOR SLAM:
 
   1. Start the launch file: roslaunch Magnum_description empty_world.launch
   2. Open RVIZ on another PC that has the same ROS master as the robot and create a visualization for the Map.
   3. Stop when satisfied.


https://user-images.githubusercontent.com/97457075/152890056-3bd7c186-5a62-4b7a-ba5e-17dc517b2f41.mp4

![slam1](https://user-images.githubusercontent.com/97457075/160631633-773af76f-3113-43fc-af1f-a765786b05ea.jpg)





https://user-images.githubusercontent.com/97457075/152890311-a8b74749-5d1e-4821-a5c6-ffa0863baa3f.mp4

