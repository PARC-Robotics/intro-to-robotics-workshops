#! /usr/bin/env python3

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist



def sensor_lidar():
    # read a message from the laser scanner device on the /scan topic
    scan_data = rospy.wait_for_message('/scan', LaserScan)
    return scan_data


def think(scan_data):
    
    # extract region of scan we are interested in -----------------------
    num_points = len(scan_data.ranges)

    fwd_range = scan_data.ranges[190:210]

    # print(fwd_range)

    # filter the data

    # compute an average distance to wall measurement -------------------
    distance_to_wall = sum(fwd_range)/len(fwd_range)

    # print(distance_to_wall)

    # condition: if distance to wall is above some threshold 6 meters, move forward
    approach_threshold = 6.0 #meters
    if distance_to_wall > approach_threshold:
        move_flag = True
    else:
        move_flag = False

    print(f'Distance to wall: {distance_to_wall}')

    return move_flag



def act(robot_vel_publisher, move_flag):
    
    # create a new Twist object
    robot_vel = Twist()

    # set the nominal forward velocity
    fwd_vel = 0.5 #m/s

    # condition: if move_flag is true, move robot
    if move_flag:
        robot_vel.linear.x = fwd_vel
        msg = "Robot Moving! \n"
    else:
        robot_vel.linear.x = 0.0
        msg = "Robot Stopped! \n"

    # publish velocity 
    robot_vel_publisher.publish(robot_vel)

    return msg



def main():

    # initialize ROS Node
    rospy.init_node('approach_barn_example')

    # set control frequency & time
    hz = 0.5 #hz
    rate = rospy.Rate(hz)
    t_start = time.time() # seconds

    # create a publisher to send velocity commands to the robot
    robot_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # setup control loop
    while not rospy.is_shutdown():

        # SENSE
        scan_data = sensor_lidar()
        

        # THINK/PLAN
        move_flag = think(scan_data)


        # ACT
        message = act(robot_vel_publisher, move_flag)



        t_elapsed = time.time() - t_start

        print(f'At time [{t_elapsed:.3f}]: {message}!')

        rate.sleep()




if __name__=='__main__':
    main()