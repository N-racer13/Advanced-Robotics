#!/usr/bin/env python
from __future__ import print_function
import rospy
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from ar_week10_test.msg import *

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "panda_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

def callback(s):
	print('----------------------------------------------------------')
	print('Move Panda - Received square size, s = ' + str(s.size))
	print('----------------------------------------------------------')
	
	#starting position
	print('Move panda - Going to start configuration')
	print('----------------------------------------------------------')
	joint_goal = move_group.get_current_joint_values()
	joint_goal[0] = 0
	joint_goal[1] = -pi/4
	joint_goal[2] = 0
	joint_goal[3] = -pi/2
	joint_goal[4] = 0
	joint_goal[5] = pi/3
	joint_goal[6] = 0
	move_group.go(joint_goal, wait=True)
	move_group.stop()
	# Path planning
	print('Move Panda - Planning motion trajectory')
	print('----------------------------------------------------------')
	waypoints = []
	wpose = move_group.get_current_pose().pose
	wpose.position.x += s.size  		# First move
	waypoints.append(copy.deepcopy(wpose))
	wpose.position.y += s.size		# Second move
	waypoints.append(copy.deepcopy(wpose))
	wpose.position.x -= s.size	  	# Third move
	waypoints.append(copy.deepcopy(wpose))
	wpose.position.y -= s.size	  	# Fourth move
	waypoints.append(copy.deepcopy(wpose))
	(plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)
	# Display trajectory
	print('----------------------------------------------------------')
	print('Move Panda - Showing planned trajectory')
	print('----------------------------------------------------------')
	display_trajectory = moveit_msgs.msg.DisplayTrajectory()
	display_trajectory.trajectory_start = robot.get_current_state()
	display_trajectory.trajectory.append(plan)
	display_trajectory_publisher.publish(display_trajectory);
	rospy.sleep(10)
	# Execute
	print('----------------------------------------------------------')
	print('Move Panda - Executing planned trajectory')
	print('----------------------------------------------------------')
	move_group.execute(plan, wait=True)
	print('Move Panda - Waiting for desired size of square trajectory')
	print('----------------------------------------------------------')


def move_panda_square():
	moveit_commander.roscpp_initialize(sys.argv)
	rospy.init_node('move_robot', anonymous=True)
	rospy.Subscriber('size', square_size, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		move_panda_square()
	except rospy.ROSInterruptException():
		pass
