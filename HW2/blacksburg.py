# ECE 2524 Homework 2 Problem 2 (Nayana Teja Chiluvuri)

import sys

with open(str(sys.argv[1]), 'r') as f:
	print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
	for line in f:
		data = line.split()	# break up each line of the input file into seperate parameters
		if data[3] == "Blacksburg":	# display the account information for the Blacksburg residents
			print data[4] + ", " + data[1] + ", "  + data[0] + ", " + data[2]

