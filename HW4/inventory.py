#!/usr/bin/env python2
# ECE 2524 Homework 4 Problem 1 (Nayana Teja Chiluvuri)

import sys
import argparse
import fileinput
import shlex

def rewriteFile():
	with open(args.data_file, "w") as f:
		for entry in entries:
			f.write('\n'.join(entry))
			f.write('\n\n')
	return

def inventory_add(arg):
	newEntry = ['']*len(entries[0])
	for index, each in enumerate(arg):
		newTerms = arg[index].split('=')
		newEntry[entries[0].index(newTerms[0])] = newTerms[1]
	entries.append(newEntry)
	print "SUCCESSFULLY ADDED NEW ENTRY:"
	print '\t'.join(newEntry)
	rewriteFile()
	return

def inventory_remove(arg):
	removeTerms = arg[0].split('=')
	for index, entry in enumerate(entries):
		if entry[entries[0].index(removeTerms[0])] == removeTerms[1]:
			print "DELETED ENTRY:"
			print '\t'.join(entry)
			del entries[index]
			inventory_remove(arg)
	rewriteFile()
	return

def inventory_set(arg):
	if arg[1] != 'for':
		return
	else:
		setTerms = arg[0].split('=')
		termToSet = arg[2].split('=')
		for entry in entries:
			if entry[entries[0].index(termToSet[0])] == termToSet[1]:
				print '\t'.join(entries[0])
				print '\t'.join(entry)
				print "CHANGED TO"
				entry[entries[0].index(setTerms[0])] = setTerms[1]
				print '\t'.join(entry)
	rewriteFile()
	return
	
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
			print '\t'.join(entry).ljust(50)

def inventory_exit(arg):
	sys.exit(0)

# argument parser
parser = argparse.ArgumentParser(description='Manipulate and display inventory from supplied datafile.')
parser.add_argument('-f', '--data-file', action='store', dest='data_file', help='enter the name of the data file')
args = parser.parse_args()


dataFile = open(args.data_file, 'r')

entry = []
entries = []
for dataLine in dataFile:
	if dataLine == '\n':
		entries.append(entry)
		entry = []
		continue
	entry.append(dataLine.strip())
dataFile.close()

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
