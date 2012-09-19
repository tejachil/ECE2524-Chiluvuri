#!/usr/bin/env python2
# ECE 2524 Homework 3 Problem 1 (Nayana Teja Chiluvuri)

import sys
import argparse

# argument parser
parser = argparse.ArgumentParser(description='Process some integers.')
args = parser.parse_args()

product = 1.0 # initialize the product to 1
while 1:
	line = sys.stdin.readline() # read each line of the stdin

	# condition for if <ENTER> is pressed on the stdin without anything being entered
	if line == '\n':
		print product
		product = 1.0
		
	# condition for the enf of file
	elif len(line) == 0:
		break

	# condition if something is entered on the stdin
	else:
		try:
			product *= float(line)
		except Exception as err: # exception if what is entered is not a number
			sys.stderr.write(str(err))
			sys.exit(1)

# print the product and exit
print product
sys.exit(0)
