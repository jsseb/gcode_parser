#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	Generate Gcode for Lissajous Curve
	Future ref will generate Gcode for other curves
'''
import numpy as np
import argparse
import matplotlib.pyplot as plt


def lissajous(a,b,rng,delta=None):
	X = []
	Y = []

	if delta == None:
		delta = ((b-1)/b) * np.pi/2
	N = (rng[1]-rng[0])/rng[2]
	for t in np.linspace(rng[0], rng[1], num=N):
		#X = a*sin(a*t + delta)
		#Y = b*sin(b*t)
		X.append(a*np.sin(a*t + delta))
		Y.append(b*np.sin(b*t))
	curve = [X,Y]
	return curve

def print_shit(curve):
	n = []
	for i in range(len(curve[0])):
		n.append([curve[0][i],curve[1][i]])
	
	f = open('lissa.txt','w')
	n = str(n)
	n = n.replace('[','')
	n = n.replace(',','')
	n = n.replace(']','\n')
	n = n.replace('\'','')
	
	f.write("{}\n".format(n))
	f.close()

def plot_shit(curve):
	plt.plot(curve[0],curve[1],'-')
	plt.show()

if __name__ == '__main__':
	#plot_shit(lissajous(2,4,[1,1 + np.pi,0.1],delta=0))
	print_shit(lissajous(2,4,[1,1 + np.pi,0.1],delta=0))