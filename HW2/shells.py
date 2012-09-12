# ECE 2524 Homework 2 Problem 1 (Nayana Teja Chiluvuri)

import sys

with open(str(sys.argv[1]), 'r') as f:
	for line in f:
		data = line.split(':') # Split each line with ':' delimiter and store each split string into a string list
		print data[0] + "\t" + data[5] # Print the username <tab> full path name
