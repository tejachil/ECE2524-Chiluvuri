#!/usr/bin/env python2
# ECE 2524 Homework 3 Problem 1 (Nayana Teja Chiluvuri)

import sys
import argparse
import fileinput

# argument parser
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('files', nargs='*', type=str, default=sys.stdin)
parser.add_argument('--ignore-blank', action='store_true', dest='ignore_blank', help='ignores the blank lines in the file')
parser.add_argument('--ignore-non-numeric', action='store_true', dest='ignore_non_numeric', help='ignores the non-numeric lines in the file')
args = parser.parse_args()

product = 1.0 # initialize the product to 1

# condition if positional arguments are supplied
if(len(sys.argv) > 1):
	for line in fileinput.input(args.files):
		# condition for if <ENTER> is pressed on the stdin without anything being entered
		if line == '\n':
			if args.ignore_blank:
				continue
			else:
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
				if args.ignore_non_numeric:
					continue
				else:
					sys.stderr.write(str(err))
					sys.exit(1)
					
# condition if no positional arguments are supplied (basically same as mult.py)
# did it like this instead of the top condition to prevent buffering problem with for line in...
else:
	while(1):
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
