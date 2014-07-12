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
try:
	import matplotlib.pyplot as plt
except:
	pass


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

def squares(a,b,n,d,change):
	X = []
	Y = []
	x = a
	y = b
	l = d
	for i in range(n):
		X.append(x)
		Y.append(y)
		X.append(x+l)
		Y.append(y)
		X.append(x+l)
		Y.append(y-l)
		X.append(x)
		Y.append(y-l)
		X.append(x)
		Y.append(y)
		x = x+change
		y = y-change
		l = l-2*change
	return [X,Y]

def lines(x,y,n,d,change):
	X = []
	Y = []

	for i in range(n):
		X.append(x+2*i)
		Y.append(y)
		X.append(x+2*i)
		Y.append(y+d+i*change)

	return [X,Y]

def print_data(curve,filename=None):

	n = [[x,y] for x,y in zip(curve[0],curve[1])]
	
	if filename is None:
		f = open('lissa.txt','w')
	else:
		f = open(filename,'w')
	n = str(n)
	n = n.replace('[','')
	n = n.replace(',','')
	n = n.replace(']','\n')
	n = n.replace('\'','')
	
	f.write("{}".format(n))
	f.close()

def plot_data(curve):
	plt.plot(curve[0],curve[1],'-')
	plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Prints and Plots the Lissajous Knot')

	parser.add_argument('--x',dest='x',required=True)
	parser.add_argument('--y',dest='y',required=True)
	parser.add_argument('--n',dest='n',required=False)
	parser.add_argument('--d',dest='d',required=False)
	parser.add_argument('--c',dest='c',required=False)

	parser.add_argument('--o',dest='option',required=True)

	parser.add_argument('--precission',dest='precission',required=False)
	parser.add_argument('--plot',dest='plot',required=False)
	parser.add_argument('--print',dest='file',required=False)
	parser.add_argument('--output',dest='filename',required=False)
	parser.add_argument('--delta',dest='delta',required=False)
	args = parser.parse_args()
	
	if args.precission is None:
		precission = 0.01
	else:
		precission = float(args.precission)
	if args.x is not None and args.y is not None:
		if args.option == 'squares':
			points = squares(int(args.x),int(args.y),int(args.n),int(args.d),int(args.c))
		if args.option == 'lines':
			points = lines(int(args.x),int(args.y),int(args.n),int(args.d),int(args.c))
		if args.option == 'lissa':
			points = lissajous(int(args.x),int(args.y),[0,2*np.pi, precission],delta = args.delta)
	if args.file is not None:
		print_data(points,filename=args.filename)
	if args.plot is not None:
		plot_data(points)