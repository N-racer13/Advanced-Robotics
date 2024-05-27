#!/usr/bin/env python
from __future__ import print_function
import rospy
import random
from ar_week10_test.msg import square_size

def square_size_generator():
	rospy.init_node('generator', anonymous=True)
	pub = rospy.Publisher('size', square_size, queue_size=10)
	rate = rospy.Rate(0.05)
	while not rospy.is_shutdown():
		size = random.uniform(0.05, 0.20)
		pub.publish(size)
		print(size)
		rate.sleep()

if __name__ == '__main__':
	try:
		square_size_generator()
	except rospy.ROSInterruptException():
		pass
