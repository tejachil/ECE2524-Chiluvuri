#!/usr/bin/env python2
# ECE 2524 Homework 4 Problem 1 (Nayana Teja Chiluvuri)

import sys
import argparse
import fileinput
import shlex

def inventory_add(arg):
	print "adding"
def inventory_remove(arg):
	print arg
def inventory_set(arg):
	if arg[1] != 'for':
		return
	else:
		setTerms = arg[0].split('=')
		termToSet = arg[2].split('=')
	
def inventory_list(arg):
	sort = False
	if arg[0] != 'all':
		return
	else:
		output = []
		if len(arg) > 2 and arg[1] == 'with':
			listTerms = arg[2].split('=')
		for entry in entries:
			if (len(arg) > 2 and arg[1] == 'with' and entry[entries[0].index(listTerms[0])] == listTerms[1]) or (len(arg) < 2) or entry == entries[0]:
				output.append(entry)
		if (len(arg) > 5 and arg[3] == 'sort' and arg[4] == 'by'):
			index = entries[0].index(arg[5])
			sort = True
		elif  (len(arg) > 3 and arg[1] == 'sort' and arg[2] == 'by'):
			output = entries
			sort = True
			index = entries[0].index(arg[3])
		if sort:
			print '\t'.join(output[0])
			output.pop(0)
			output.sort(key=lambda k: k[index])
		for entry in output:
			print '\t'.join(entry)


def inventory_exit(arg):
	sys.exit(0)

# argument parser
parser = argparse.ArgumentParser(description='Manipulate and display inventory from supplied datafile.')
parser.add_argument('-f', '--data-file', action='store', dest='data_file', help='enter the name of the data file')
args = parser.parse_args()

dataFile = open(args.data_file)

entry = []
entries = []
for dataLine in dataFile:
	if dataLine == '\n':
		entries.append(entry)
		entry = []
		continue
	entry.append(dataLine.strip())


while True:
	try:
		inputLine = sys.stdin.readline()
		arguments = shlex.split(inputLine)
		command = arguments[0]
		arguments.pop(0)
	except KeyboardInterrupt:
		sys.exit(0)
	if not inputLine:
		continue

	commandActions = {'add': inventory_add, 'remove': inventory_remove, 'subtract': inventory_remove, 'set': inventory_set, 'update': inventory_set, 'list': inventory_list, 'view': inventory_list, 'display': inventory_list, 'exit': inventory_exit, 'quit': inventory_exit}
	try:
		commandActions[command](arguments)
	except KeyError as e:
		sys.stderr.write("Invalid command: {}\n".format(command))
