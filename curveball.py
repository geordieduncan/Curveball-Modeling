#!python2.7
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def pos(v, w, phi, theta, s, n, m = 0.145, r = 0.03734):
	global fig
	global ax
	x = [0.0]
	y = [0.0]
	z = [0.0]
	xv = math.sin(phi)*math.cos(theta)*v
	yv = math.cos(phi)*math.sin(theta)*v
	zv = math.cos(phi)*math.cos(theta)*v
	while(z[-1] < 18.47):
		x.append(x[-1]+xv/n)
		y.append(y[-1]+yv/n)
		z.append(z[-1]+zv/n)
		yv-= 9.8/n
		V = math.sqrt(xv**2+yv**2+zv**2)
		Fm = V*w*(4*math.pi/3)*(r**3)/m
		xc = yv*zv/math.sqrt((yv**2*zv**2)+(zv*xv*math.tan(theta+(math.sin(s)*math.pi)))**2+(yv*xv*math.tan(phi+(math.cos(s)*math.pi)))**2)
		yc = (zv*xv*math.tan(theta+(math.sin(s)*math.pi)))/math.sqrt((yv**2*zv**2)+(zv*xv*math.tan(theta+(math.sin(s)*math.pi)))**2+(yv*xv*math.tan(phi+(math.cos(s)*math.pi)))**2)
		zc = (yv*xv*math.tan(phi+(math.cos(s)*math.pi)))/math.sqrt((yv**2*zv**2)+(zv*xv*math.tan(theta+(math.sin(s)*math.pi)))**2+(yv*xv*math.tan(phi+(math.cos(s)*math.pi)))**2)
		xv += xc*Fm/n
		yv += yc*Fm/n
		zv += zc*Fm/n
		print '%f, %f, %f' %(x[-1],y[-1],z[-1])
	ax.plot(np.array(x),np.array(z),np.array(y))
	ax.set_xlim3d([-2.0, 2.0])
	ax.set_xlabel('X')
	ax.set_ylim3d([0.0, 20.0])
	ax.set_ylabel('Y')
	ax.set_zlim3d([-2.0, 2.0])
	ax.set_zlabel('Z')
	ax.set_title('Curveball')
	plt.show()
	return [x,y,z]

dat = pos(42.0, 50.0, math.pi/326, math.pi/128, 0.0, 250.0)

def show():
	ax.view_init(elev = 0.0, azim = 90.0)
	plt.show()

def analyze(v, w, phi, theta, n, N = 5, m = 0.145, r = 0.03734):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	for i in range(N):
		dat = pos(v, w, phi, theta, 2*i*math.pi/N, n)
	ax.set_xlim3d([-2.0, 2.0])
	ax.set_xlabel('X')
	ax.set_ylim3d([0.0, 20.0])
	ax.set_ylabel('Y')
	ax.set_zlim3d([-2.0, 2.0])
	ax.set_zlabel('Z')
	ax.set_title('3D Test')
	ax.view_init(elev = 0.0, azim = 90.0)
	plt.show()
	return 'Done'