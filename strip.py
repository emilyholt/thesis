#!/usr/bin/env python
import re

f = open("reports.txt", "r")
data = f.read()
f.close()

f = open("stripped.txt", "w")

reports = data.split('======================================================')

for r in reports:
	match = re.search("Current Votes", r)
	if match :
		#replace everything after Current Votes with ''
		impt_stuff = r.split("Current Votes")[0]
		f.write(impt_stuff)
		f.write('======================================================')
	else :
		f.write(r)
		f.write('======================================================')
f.close()