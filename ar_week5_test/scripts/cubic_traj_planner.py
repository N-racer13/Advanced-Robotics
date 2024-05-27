#!/usr/bin/env python
from __future__ import print_function
import rospy
import numpy as np
from ar_week5_test.msg import *
from ar_week5_test.srv import *

def callback(params):
	rospy.wait_for_service('compute_cubic_coeffs')
	rate = rospy.Rate(10)
	try:
		cubic_coeffs = rospy.ServiceProxy('compute_cubic_coeffs', compute_cubic_traj)
		resp = cubic_coeffs(params)
		resp2 = cubic_traj_coeffs()
		resp2.a0 = resp.a0
		resp2.a1 = resp.a1
		resp2.a2 = resp.a2
		resp2.a3 = resp.a3
		resp2.t0 = params.t0
		resp2.tf = params.tf
		pub = rospy.Publisher('coefficients', cubic_traj_coeffs, queue_size=10)
		pub.publish(resp2)
		rate.sleep()
	
	except rospy.ROSInterruptException():
		pass

def cubic_traj_planner():
	rospy.init_node('planner', anonymous=True)
	rospy.Subscriber('parameters', compute_cubic_trajRequest, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		cubic_traj_planner()
	except rospy.ROSInterruptException():
		pass
