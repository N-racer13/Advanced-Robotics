#!/usr/bin/env python
from __future__ import print_function
import rospy
import random
from ar_week5_test.msg import cubic_traj_params


def points_generator():
	rospy.init_node('generator', anonymous=True)
	pub = rospy.Publisher('parameters', cubic_traj_params, queue_size=10)
	rate = rospy.Rate(0.05)
	while not rospy.is_shutdown():
		p0 = random.uniform(-10, 10)
		pf = random.uniform(-10, 10)
		v0 = random.uniform(-10, 10)
		vf = random.uniform(-10, 10)
		t0 = 0
		tf = random.uniform(5, 10)
		pub.publish(p0, pf, v0, vf, t0, tf)
		rate.sleep()

if __name__ == '__main__':
	try:
		points_generator()
	except rospy.ROSInterruptException():
		pass
