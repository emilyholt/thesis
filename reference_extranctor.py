#!/usr/bin/env python
import re
import operator
# *************************************************************************

# Extract reports from 2014
f = open("allitems.txt", "r")
data = f.read()
f.close()
reports = data.split('======================================================')

#get CVE number and map it to number of references
dictionary = {}

for r in reports : 
	name = r.split('\nStatus')[0]
	id_num = name.split(": ")[1]
	references = r.count("Reference:")
	dictionary[id_num] = references

count = 1
sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse = True)
for key in sorted_dictionary :
	print str(count) + " : " + str(key)
	count += 1
	if count == 11 : 
		break 


