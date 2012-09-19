#!/usr/bin/env python2
# ECE 2524 Homework 3 Problem 1 (Nayana Teja Chiluvuri)

import sys
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
args = parser.parse_args()

product = 1.0
while 1:
	line = sys.stdin.readline()
	if line == '\n':
		print product
		product = 1.0
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
