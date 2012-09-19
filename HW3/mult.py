#!/usr/bin/env python2
# ECE 2524 Homework 3 Problem 1 (Nayana Teja Chiluvuri)

import sys

if len(sys.argv) == 2 and (str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help"):
	print "usage: %s [%s]" % (sys.argv[0], sys.argv[1])
	print "\nProcess some numbers.\n"
	print "optional arguments:"
	print "\t-h, --help show this help message and exit"
	sys.exit(0)
elif len(sys.argv) == 1:
	product = 1
	while 1:
		line = sys.stdin.readline()
		if line == '\n':
			print product
			product = 1
		elif len(line) == 0:
			break
		else:
			try:
				product *= float(line)
			except Exception as err:
				sys.stderr.write(str(err))
				sys.exit(1)
	print product
	sys.exit(0)
else:
	print "usage: %s [-h]" % sys.argv[0]
	err = "%s: error: unrecognized arguments:" % sys.argv[0]
	for i in range(1,len(sys.argv)):
		err += ' ' + sys.argv[i]
	err += '\n'
	sys.stderr.write(err)
	sys.exit(2)
