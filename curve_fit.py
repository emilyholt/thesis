#!/usr/bin/env python
import re
import operator
import sys
from pylab import *
import numpy as np
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

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


# # plot(years, vulns)
# xlabel('Years')
# ylabel('Number of reported vulnerabilities')
# title(keyword + ' Vulnerabilities reported per year')
# savefig(keyword + "_analysis.png")
# show()

# points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])
# # get x and y vectors
# x = points[:,0]
# y = points[:,1]

# calculate polynomial
z = np.polyfit(years, vulns, 3)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(years[0], years[-1], 50)
y_new = f(x_new)

plt.plot(years, vulns, 'o', x_new, y_new)
plt.xlim([years[0]-1, years[-1] + 1 ])
plt.show()