#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import argparse
import numpy as np

def calibrate(gcode, ratio, var=None):
	"""
		Searching for gcode numbers, multiply by ratio.
		var indicates a specific letter to calibrate
	"""
	pass

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

	f = open('stub.ngcode', 'w')
	f.write("{}\n".format(n))
	f.close()

	#with open('stub.ngcode', 'r') as f, open(filename,'w') as out:
	#for line in f:
	#	line = re.sub(r'^.$', lambda m: 'c' + m.groups()[0],line)

	#f.close()

def load_coord(filename):
	pass

def load_gcode(filename):
	u_gcode = []
	f = open(filename, 'r')
	for line in f:
		u_gcode.append(line.split())
	f.close()

	#Clean all lines that dont start with G0 or G1
	#Clean all A# and F# attributes
	gcode = []
	#pattern = re.compile("\\b(F|A)\\W",re.I)
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
	parser.add_argument('--loops',dest='loops',required=False)
	parser.add_argument('--calibrate',dest='ratio',required=False)
	parser.add_argument('--var',dest='var',required=False)
	parser.add_argument('--coord',dest='coord',required=False)
	args = parser.parse_args()

	if (args,'file'):
		filename = args.file
	else:
		if hasattr(args,'coord'):
			filename = args.coord
		else:
			raise Exception("Error loading File")
			return -1

	if hasattr(args,'calibrate'):
		if hasattr(args,'var'):
			gcode = calibrate(gcode,args.calibrate,var=args.var)
		else:
			gcode = calibrate(gcode,args.calibrate)

	if hasattr(args,'loops'):
		if args.loops > 1:
			gcode = loop(gcode,int(args.loops))

	gcode = load_gcode(filename)
	save_gcode(gcode,'stub2.gcode')
	

if __name__ == '__main__':
	main()