#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	Generate Gcode for Lissajous Curve
	Future ref will generate Gcode for other curves

	Test range : [1,1 + np.pi,0.1]
	Test delta : 0
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
	
	f.write("{}".format(n))
	f.close()

def plot_shit(curve):
	plt.plot(curve[0],curve[1],'-')
	plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Prints and Plots the Lissajous Knot')

	parser.add_argument('--x',dest='x',required=True)
	parser.add_argument('--y',dest='y',required=True)
	parser.add_argument('--precission',dest='precission',required=False)
	parser.add_argument('--plot',dest='plot',required=False)
	parser.add_argument('--output',dest='file',required=False)
	parser.add_argument('--delta',dest='delta',required=False)
	args = parser.parse_args()
	
	if args.precission is None:
		precission = 0.1
	else:
		precission = args.precission
	if args.x is not None and args.y is not None:
		l = lissajous(int(args.x),int(args.y),[0,2*np.pi, precission],delta = args.delta)
	if args.file is not None:
		print_shit(l)
	if args.plot is not None:
		plot_shit(l)