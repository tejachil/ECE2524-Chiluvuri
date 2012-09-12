# ECE 2524 Homework 2 Problem 3 (Nayana Teja Chiluvuri)

import sys

with open(str(sys.argv[1]), 'r') as f:
	# initialize variabled for scope and definition of data type
	maxAmount = 0
	minAmount = 0
	maxName = ""
	minName = ""
	totalAmount = 0
	counter = 0;
	for line in f:
		data = line.split()	# break up each line of the input file into seperate parameters
		totalAmount += float(data[2]);
		counter+=1
		# determine if the current line has a max amount owed
		if maxAmount == 0 or float(data[2]) > maxAmount:
			maxAmount = float(data[2])
			maxName = data[1]
		# determine if the current line has a min amount owed
		if minAmount == 0 or float(data[2]) < minAmount:
			minAmount = float(data[2])
			minName = data[1]
	if counter != 0:
		averageAmount = totalAmount/counter	# calculate the average amount owed
		# print the account summary in the specified format
		print "ACCOUNT SUMMARY"
		print "Total amount owed = %.2f" % totalAmount
		print "Average amount owed = %.2f" % averageAmount
		print "Maximum amount owed = %.2f by %s" % (maxAmount, maxName)
		print "Minimum amount owed = %.2f by %s" % (minAmount, minName)
