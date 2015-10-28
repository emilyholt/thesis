#!/usr/bin/env python
from __future__ import division, unicode_literals
import re
import math
from textblob import TextBlob as tb

def tf(word, blob):
	wordlist = re.sub("[^\w]", " ", blob).split()
	return wordlist.count(word) / len(wordlist)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

f = open("reports.txt", "r")
data = f.read()
f.close()

# reports = data.split('======================================================')

# for r in reports:
# 	match = re.search("Current Votes", r)
# 	if match :
# 		#replace everything after Current Votes with ''
# 		impt_stuff = r.split("Current Votes")[0]
# 		r = impt_stuff

f = open("stripped.txt", "w")

reports = data.split('======================================================')

for r in reports:
	match = re.search("Current Votes", r)
	if match :
		#replace everything after Current Votes with ''
		impt_stuff = r.split("Current Votes")[0]
		f.write(impt_stuff)
	else: 
		f.write(r)

bloblist = reports
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    wordlist = re.sub("[^\w]", " ", blob).split()
    for word in wordlist:
    	scores = {word: tfidf(word, blob, bloblist)}
    # scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
	sw = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sw[:3]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))