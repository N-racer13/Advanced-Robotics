#!/usr/bin/env python
from __future__ import print_function
import rospy
import numpy as np
from ar_week5_test.srv import compute_cubic_traj, compute_cubic_trajResponse


def compute_cubic_coeffs(req):
	p0 = req.p0
	pf = req.pf
	v0 = req.v0
	vf = req.vf	
	t0 = req.t0
	tf = req.tf
	M = np.array([[1, t0, t0**2, t0**3], [0, 1, 2*t0, 3*t0**2], [1, tf, tf**2, tf**3], [0, 1, 2*tf, 3*tf**2]])
	Minv = np.linalg.inv(M)
	c = np.array([p0, v0, pf, vf])
	c = np.transpose(c)
	a = np.matmul(Minv, c)
	resp = compute_cubic_trajResponse()
	resp.a0 = a[0]
	resp.a1 = a[1]
	resp.a2 = a[2]
	resp.a3 = a[3]
	return(resp)

def compute_cubic_coeffs_server():
	rospy.init_node('server', anonymous=True)
	s = rospy.Service('compute_cubic_coeffs', compute_cubic_traj, compute_cubic_coeffs)
	rospy.spin()

if __name__ == '__main__':
	try:
		compute_cubic_coeffs_server()
	except rospy.ROSInterruptException():
		pass
