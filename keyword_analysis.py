#!/usr/bin/env python
import re
import operator
import sys
from pylab import *
import numpy as np
from scipy.optimize import curve_fit

# curve function
def func(x, p1,p2):
  return p1*np.cos(p2*x) + p2*np.sin(p1*x)



keyword = sys.argv[1]

inputfile = keyword + "_reports.txt"
f = open(inputfile, "r")
data = f.read()
f.close()

 # *************************************************************************

reports = data.split('======================================================')
dictionary = {}
years = []
vulns = []

print "Number of reports: " + str(len(reports))

for r in reports : 
	# Name: CVE-1999-0001
	found = re.search('-(.+?)-', r)
	if found:
		val = found.group(1)
	if dictionary.has_key(val) :
		count = dictionary[val] 
		count += 1
		dictionary[val] = count
	else :
		dictionary[val] = 1



for key in sorted(dictionary.iterkeys()):
	years.append(int(key))
	vulns.append(dictionary[key])

fig = figure()
ax = subplot(111)
ax.bar(years, vulns, width=1)

# plot(years, vulns)
xlabel('Years')
ylabel('Number of reported vulnerabilities')
title(keyword + ' Vulnerabilities reported per year')
savefig(keyword + "_analysis.png")
show()



