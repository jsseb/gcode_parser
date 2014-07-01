#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse

def calibrate(gcode, ratio, var=None):
	"""
		Searching for gcode numbers, multiply by ratio.
		var indicates a specific letter to calibrate
	"""
	pass

def loop(gcode,loops):
	return gcode = [gcode.append[gcode] for x in range(loops)]

def save_gcode(gcode, filename):
	# Append initial words
	"""
		G28 ; home all axes
		G90 ; use absolute coordinates
	"""
	gcode = ['G28 ; home all axes','G90 ; use absolute coordinates'].append(gcode)
	# Append final words
	"""
		G28 ; home all axes
		M84 ; disable motors
	"""
	gcode.append(['G28 ; home all axes'],['M84 ; disable motors'])

	f = open(filename, 'w')
	for line in gcode:
		f.write("%s\n" % line)
		#f.write("{}\n".format(line))
	f.close()

def load_gcode(filename):
	u_gcode = []
	f = open(filename, 'r')
	for line in f:
		u_gcode.append(line.split())
	f.close()

	#Clean all lines that dont start with G0 or G1
	gcode = []
	for line in u_gcode:
		if line[0] == "G0" or "G1":
			gcode.append(line)
	print (gcode)
	return gcode

def main(filename=None):
	parser = argparse.ArgumentParser(description='Convert Slic3r gcode')

	parser.add_argument('--file',dest='file',required=True)

	args = parser.parse_args()

	if filename == None:
		filename = args.file

	gcode = load_gcode(filename)
	

if __name__ == '__main__':
	main(sys.argv)