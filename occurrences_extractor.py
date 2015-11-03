#!/usr/bin/env python
import re
import operator
# *************************************************************************

# Extract reports from 2014
f = open("allitems.txt", "r")
data = f.readlines()
f.close()
# reports = data.split('======================================================')

#get every occurrence of CVE-xxxx-xxxx and map its to number of occurrences
dictionary = {}

for line in data :
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


