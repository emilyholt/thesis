#!/usr/bin/env python
import re
import operator
import sys

keyword = sys.argv[1]

f = open("allitems.txt", "r")
data = f.read()
f.close()

 # *************************************************************************

output = keyword + "_reports.txt"
f = open(output, "w")
reports = data.split('======================================================')

for r in reports : 
	match = re.search(keyword, r)

	if match :
		f.write(r)
		f.write('======================================================')

f.close()


