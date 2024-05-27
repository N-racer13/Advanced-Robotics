#!/usr/bin/env python
from __future__ import print_function
import rospy
import time
from std_msgs.msg import Float32
from ar_week5_test.msg import *

def callback(coeffs):
	a0 = coeffs.a0
	a1 = coeffs.a1
	a2 = coeffs.a2
	a3 = coeffs.a3
	t0 = coeffs.t0
	tf = coeffs.tf
	pub_pos = rospy.Publisher('position', Float32, queue_size=10)
	pub_vel = rospy.Publisher('velocity', Float32, queue_size=10)
	pub_acc = rospy.Publisher('acceleration', Float32, queue_size=10)
	t = t0
	starttime = time.time()
	while t < tf:
		pos = a0 + a1*t + a2*t**2 + a3*t**3
		vel = a1 + 2*a2*t + 3*a3*t**2
		acc = 2*a2 + 6*a3*t
		pub_pos.publish(pos)
		pub_vel.publish(vel)
		pub_acc.publish(acc)
		t = time.time() - starttime

def plot_cubic_traj():
	rospy.init_node('plotter', anonymous=True)
	rospy.Subscriber('coefficients', cubic_traj_coeffs, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		plot_cubic_traj()
	except rospy.ROSInteruptException:
		pass
