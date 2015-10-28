#!/usr/bin/env python
import re
from pylab import *

input = open("allitems.txt", "r")

dictionary = {}
years = []
vulns = []

for line in input :
	match = re.match('Name:', line)
	if match:
		# Name: CVE-1999-0001
		found = re.search('-(.+?)-', line)
		if found:
			val = found.group(1)
		if dictionary.has_key(val) :
			count = dictionary[val] 
			count += 1
			dictionary[val] = count
		else :
			dictionary[val] = 1

for key in sorted(dictionary.iterkeys()):
	years.append(key)
	vulns.append(dictionary[key])

plot(years, vulns)
xlabel('Years')
ylabel('Number of reported vulnerabilities')
title('Vulnerabilities reported per year')
savefig("output.png")
show()



