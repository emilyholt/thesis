#!/usr/bin/env python
from __future__ import division, unicode_literals
import re
import math
from textblob import TextBlob as tb

f = open("allitems.txt", "r")
data = f.read()
f.close()

 # *************************************************************************

# Extract reports from 2006
f = open("2006.txt", "w")
reports = data.split('======================================================')

for r in reports : 
	correct_year = re.search('Name: CVE-2006', r)

	if correct_year :
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
# *************************************************************************

f = open("2006.txt", "r")
lines = f.readlines()
f.close()

f = open("parsed2006.txt", "w")
for line in lines :
	
	match_name = re.match('Name:', line)
	match_status = re.match('Status:', line)
	match_url = re.match('URL:', line)
	match_phase = re.match('Phase:', line)
	match_category = re.match('Category:', line)
	match_reference = re.match('Reference:', line)
	
	if not (match_name or match_status or match_url or match_phase or match_category or match_reference):

		f.write(line)

f.close()

# *************************************************************************

f = open("parsed2006.txt", "r")
info = f.read()
bloblist = info.split('======================================================')

def tf(word, blob):
	wordlist = re.sub("[^\w]", " ", blob).split()
	return wordlist.count(word) / len(wordlist)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    wordlist = re.sub("[^\w]", " ", blob).split()
    for word in wordlist:
    	scores = {word: tfidf(word, blob, bloblist)}
    # scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
	sw = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sw[:3]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
