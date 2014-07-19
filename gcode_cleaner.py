#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import argparse

def invert_axis(gcode,axis):
	'''
		Select an Axis. Invert the drawing
		Future: Move the drawing freely. Select origin point
	'''
	pass

def calibrate(gcode, ratio, var=None):
	"""
		Searching for gcode numbers, multiply by ratio.
		var indicates a specific letter to calibrate
	"""
	ngcode = []
	for line in gcode:
		l = []
		for c in line.split():
			if c.find('X') is 0:
				aux = c.replace("X"," ")
				aux = float(aux)*ratio
				c = "{0:.4}".format(aux)
			if c.find('Y') is 0:
				aux = c.replace("Y"," ")
				aux = float(aux)*ratio
				c = "{0:.4}".format(aux)
			try:
				l.append(c)
				print (l)
			except:
				pass
		ngcode.append(l)

	return ngcode

def loop(gcode,loops):
	return [gcode.append[gcode] for x in range(loops)]

def save_gcode(gcode, filename):
	# Append initial words
	"""
		G28 ; home all axes
		G90 ; use absolute coordinates
	"""
	l = [['G28 ; home all axes'],['G90 ; use absolute coordinates']]
	gcode = l + gcode
	# Append final words
	"""
		G28 ; home all axes
		M84 ; disable motors
	"""
	gcode.append(['G28 ; home all axes'])
	gcode.append(['M84 ; disable motors'])

	n = str(gcode)
	n = n.replace('[','')
	n = n.replace(',','')
	n = n.replace(']','\n')
	n = n.replace('\'','')

	f = open(filename, 'w')
	f.write("{}".format(n))
	f.close()


def load_coord(filename):
	gcode = []
	f = open(filename,'r')
	try:
		for line in f:
			l = line.split()
			gcode.append("G1 X" + "{0:.4}".format(float(l[0])) + " Y" + "{0:.4}".format(float(l[1])) + " ]" )
	except:
		pass
	f.close()

	gcode[0].replace("G1","G0")
	return gcode

def load_gcode(filename):
	u_gcode = []
	f = open(filename, 'r')
	for line in f:
		u_gcode.append(line.split())
	f.close()

	#Clean all lines that dont start with G0 or G1
	#Clean all A# and F# attributes
	gcode = []
	pattern = re.compile('A[0-9]*.[0-9]*|F[0-9]*.[0-9]*')

	for line in u_gcode:
		if len(line) > 0:
			if line[0] == "G0" or line[0] == "G1":
				#gcode.append([re.sub(pattern,"",word) for word in line])
				words = []
				for word in line:
					if not re.search(pattern,word):
						words.append(word)
				gcode.append(words)

	return gcode

def main():
	parser = argparse.ArgumentParser(description='Convert Slic3r gcode')

	parser.add_argument('--file',dest='file',required=False)
	parser.add_argument('--output',dest='output',required=False)
	parser.add_argument('--loops',dest='loops',required=False)
	parser.add_argument('--calibrate',dest='calibrate',required=False)
	parser.add_argument('--var',dest='var',required=False)
	parser.add_argument('--coord',dest='coord',required=False)

	args = parser.parse_args()
				
	if args.file is not None:
		gcode = load_gcode(args.file)
	else:
		if args.coord is not None:
			gcode = load_coord(args.coord)
		else:
			raise Exception("Error loading File")
			return -1

	if args.calibrate is not None:
		if args.var is not None:
			gcode = calibrate(gcode,float(args.calibrate),var=args.var)
		else:
			gcode = calibrate(gcode,float(args.calibrate))

	if args.loops is not None:
		if args.loops > 1:
			gcode = loop(gcode,int(args.loops))

	if args.output is not None:
		save_gcode(gcode, args.output)
	else:
		save_gcode(gcode,'stub.gcode')
	

if __name__ == '__main__':
	main()
