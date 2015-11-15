#!/usr/bin/env python
import re
import operator
import sys
import numpy as np
from pylab import *

keyword1 = sys.argv[1]
keyword2 = sys.argv[2]
keyword3 = sys.argv[3]

inputfile1 = keyword1 + "_reports.txt"
inputfile2 = keyword2 + "_reports.txt"
inputfile3 = keyword3 + "_reports.txt"

f1 = open(inputfile1, "r")
f2 = open(inputfile2, "r")
f3 = open(inputfile3, "r")

data1 = f1.read()
data2 = f2.read()
data3 = f3.read()

f1.close()
f2.close()
f3.close()

 # *************************************************************************

reports1 = data1.split('======================================================')
reports2 = data2.split('======================================================')
reports3 = data3.split('======================================================')

years = []
vulns1 = []
vulns2 = []
vulns3 = []

for i in range(1999, 2016) :
	years.append(i)
	vulns1.append(0)
	vulns2.append(0)
	vulns3.append(0)

print "Number of reports for " + keyword1 + ": " + str(len(reports1))
print "Number of reports for " + keyword2 + ": " + str(len(reports2))
print "Number of reports for " + keyword3 + ": " + str(len(reports3))

for r in reports1 : 
	# Name: CVE-1999-0001
	found = re.search('-(.+?)-', r)
	if found:
		val = found.group(1)
		index = int(val) - 1999
		count = vulns1[index] 
		count += 1
		vulns1[index] = count

for r in reports2 : 
	# Name: CVE-1999-0001
	found = re.search('-(.+?)-', r)
	if found:
		val = found.group(1)
		index = int(val) - 1999
		count = vulns2[index] 
		count += 1
		vulns2[index] = count

for r in reports3 : 
	# Name: CVE-1999-0001
	found = re.search('-(.+?)-', r)
	if found:
		val = found.group(1)
		index = int(val) - 1999
		count = vulns3[index] 
		count += 1
		vulns3[index] = count

# plot(years, vulns)

N = len(years)
ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind, vulns1, width, color='r')
rects2 = ax.bar(ind + width, vulns2, width, color='y')
rects3 = ax.bar(ind + 2 * width, vulns3, width, color='b')

#labels
title(keyword1 + ' vs ' + keyword2 + 'vs' + keyword3 + ' Vulnerabilities reported per year')
ax.set_ylabel('Number of reported vulnerabilities')
ax.set_xlabel('Years since 1999')
ax.set_title(keyword1 + ' vs ' + keyword2 + ' vs ' + keyword3 + ' Vulnerabilities reported per year')

#legend
ax.legend((rects1[0], rects2[0], rects3[0]), (keyword1, keyword2, keyword3), loc=0)

savefig(keyword1 + '_' + keyword2 + '_' + keyword3 + "_analysis.png")
show()



