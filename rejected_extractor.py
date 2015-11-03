#!/usr/bin/env python
import re
import operator

f = open("allitems.txt", "r")
data = f.read()
f.close()

 # *************************************************************************

# Extract reports from 2006
f = open("rejected_reports.txt", "w")
reports = data.split('======================================================')

for r in reports : 
	rejected = re.search('REJECT', r)

	if rejected :
		f.write(r)
		f.write('======================================================')

f.close()

# *************************************************************************

f = open("rejected_reports.txt", "r")
lines = f.readlines()
f.close()

dictionary = {}

for line in lines :
	cve_match = re.match(r'CVE-\d{4}-\d{4}', line)

	if cve_match :
		name = cve_match.group()
		if name in dictionary :
			occurrences = dictionary[name] + 1
		else :
			occurrences = 1
		dictionary[name] = occurrences


count = 1
sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse = True)
for key in sorted_dictionary :
	print str(count) + " : " + str(key)
	count += 1
	if count == 11 : 
		break 
