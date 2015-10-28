#!/usr/bin/env python
import re

f = open("reports.txt", "r")
lines = f.readlines()
f.close()

f = open("reports.txt", "w")
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