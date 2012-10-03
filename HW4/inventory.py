#!/usr/bin/env python2
# ECE 2524 Homework 4 Problem 1 (Nayana Teja Chiluvuri)

import sys
import argparse
import fileinput
import shlex

# Function that displays the entries in a table looking layout
def printEntry(entryArg):
	# Get the size of the biggest string displayed in each column
	columnSize = [0]*len(headings)
	for index, col in enumerate(headings):
		columnSize[index] = len(col)
	for entry in entries:
		for index, each in enumerate(entry):
			if len(str(each)) > columnSize[index]:
				columnSize[index] = len(each)
	outputPrint = ''
	
	# Concatenate the columns into a string based on the spacing from above
	for index, elem in enumerate(entryArg):
		outputPrint += str(elem).ljust(columnSize[index]+3)
	return outputPrint

# Updates the contents of the data file based on the data in the entries data structure
def rewriteFile():
	with open(args.data_file, "w") as f:
		for col in headings:
			f.write(str(col))
			f.write('\n')
		f.write('\n')
		for entry in entries:
			for elem in entry:
				f.write(str(elem))
				f.write('\n')
			f.write('\n')
	return

# Function that carries out the add command
def inventory_add(arg):
	newEntry = ['']*len(headings)
	try:
		for index, each in enumerate(arg):
			newTerms = arg[index].split('=')
			# Store quantities as integers so that they can be sorted accordingly
			if headings[index] == 'Quantity':
				print newEntry
				newEntry[headings.index(newTerms[0])] = int(newTerms[1])
			else:
				newEntry[headings.index(newTerms[0])] = newTerms[1]
		entries.append(newEntry)
	except ValueError:
		print "Error: Unable to add entry. Invalid field entered."
		return
	print "SUCCESSFULLY ADDED NEW ENTRY:"
	print printEntry(newEntry)
	rewriteFile()
	return

# Function that carries out the remove command and deletes the entry specified
def inventory_remove(arg):
	removeTerms = arg[0].split('=')
	try:
		for index, entry in enumerate(entries):
			if str(entry[headings.index(removeTerms[0])]) == removeTerms[1]:
				print "DELETED ENTRY:"
				print printEntry(entry)
				del entries[index]
				inventory_remove(arg)
	except ValueError:
		print "Error: Unable to delete entry. Entry does not exist."
		return
	rewriteFile()
	return

# Function that carries out the set command and sets a specific field in a specific entry
def inventory_set(arg):
	if arg[1] != 'for':
		return
	else:
		try:
			setTerms = arg[0].split('=')
			termToSet = arg[2].split('=')
			for entry in entries:
				if entry[headings.index(termToSet[0])] == termToSet[1]:
					print printEntry(headings)
					print printEntry(entry)
					print "CHANGED TO"
					# Store quantities as integers so that they can be sorted accordingly
					if headings[headings.index(termToSet[0])] == 'Quantity':
						entry[headings.index(setTerms[0])] = int(setTerms[1])
					else:
						entry[headings.index(setTerms[0])] = setTerms[1]
					print printEntry(entry)
		except ValueError:
			print "Error: Unable to update entry. Entry does not exist."
			return
	rewriteFile()
	return

# Function that carries out the list and sort commands
def inventory_list(arg):
	sort = False
	if arg[0] != 'all':
		return
	else:
		output = []
		try:
			# List command with or without the 'with' keyword and parameters
			listTerms = ['','']
			if len(arg) > 2 and arg[1] == 'with':
				listTerms = arg[2].split('=')
			for entry in entries:
				if (len(arg) > 2 and arg[1] == 'with' and str(entry[headings.index(listTerms[0])]) == listTerms[1]) or (len(arg) < 2):
					output.append(entry)
		except ValueError:
			print "Error: Unable to list."
			return
		index = [0]*2
		
		# List command with the 'with' keyword AND the 'sort by' keyword
		if (len(arg) > 5 and arg[3] == 'sort' and arg[4] == 'by'):
			try:
				index[0] = headings.index(arg[5])
			except ValueError:
				print "Error: Invalid field to sort by."
				return
			sort = True
			
		# List command with just the 'sort by' keyword and perameters
		elif  (len(arg) > 3 and arg[1] == 'sort' and arg[2] == 'by'):
			output = entries
			try:
				index[0] = headings.index(arg[3])
			except ValueError:
				print "Error: Invalid field to sort by."
				return
			sort = True
		if sort:
			# EXTRA CREDIT implementation
			# 	sorts by PartID as a secondary sort to the one specified
			#	if primary sort by perameter is PartID, then sorts by the Description
			if index[0] == 0:
				index[1] = 1
			output = sorted(output, key=lambda k: (k[index[0]], k[index[1]]))
			sort = False
		print printEntry(headings)
		for entry in output:
			print printEntry(entry)
	return

# Function to exit program with no errors on the exit command
def inventory_exit(arg):
	sys.exit(0)

# argument parser
parser = argparse.ArgumentParser(description='Manipulate and display inventory from supplied datafile.')
parser.add_argument('-f', '--data-file', action='store', dest='data_file', help='enter the name of the data file')
args = parser.parse_args()


# Initially open the data file and store all of it's contents in the entires and headings data structures
try:
	dataFile = open(args.data_file, 'r')
except IOError:
	sys.stderr.write("Error: Input data file does not exist.\n")
	sys.exit(1)

entry = []
entries = []
headings = []

# Store headings into headings list
for dataLine in dataFile:
	if dataLine == '\n':
		break
	headings.append(dataLine.strip())

#Store entries into entires list of a list
indexCount = 0
for dataLine in dataFile:
	if dataLine == '\n':
		entries.append(entry)
		indexCount = 0
		entry = []
		continue
	# Store quantities as integers so that they can be sorted accordingly
	if headings[indexCount] == 'Quantity':
		entry.append(int(dataLine.strip()))
	else:
		entry.append(dataLine.strip())
	indexCount += 1
dataFile.close()

# MAIN loop of execution
while True:
	try:
		print '\nPLEASE ENTER A COMMAND: '
		inputLine = sys.stdin.readline()
		print '\tCOMMAND ENTERED: ' + inputLine
		if inputLine.strip():
			arguments = shlex.split(inputLine)
			command = arguments[0]		
			arguments.pop(0)
		else:
			continue
	except KeyboardInterrupt:
		sys.exit(0)

	# My Dictionary of acceptable commands
	commandActions = {'add': inventory_add, 'remove': inventory_remove, 'subtract': inventory_remove, 'set': inventory_set, 'update': inventory_set, 'list': inventory_list, 'view': inventory_list, 'display': inventory_list, 'exit': inventory_exit, 'quit': inventory_exit}
	try:
		commandActions[command](arguments)
	except KeyError as e:
		sys.stderr.write("Invalid command: {}\n".format(command))
