#!/usr/bin/env python3

import csv
import json

address = 9021
index = 0.03820489834

padding = 0.002


out = {}

out['index'] = index
out['photo-years'] = []

reels = [{ 'year': '1966', 'src': '2012m1_ref199_241' },
    { 'year': '1973', 'src': '2012m1_ref32_4a7' },
    { 'year': '1985', 'src': '2012m1_ref67_835' },
    { 'year': '1995', 'src': '2012m1_ref79_8u9' },
    { 'year': '2007', 'src': '2012m2_ref33_oy0' }]


for r in reels:

	thisYear = {}
	thisYear['year'] = r['year']
	thisYear['photos'] = []

	photoReelCsv = open(r['src']+"-n.csv",'r')
	photoReelData = csv.DictReader(photoReelCsv)

	for photo in photoReelData:
		if float(photo['index']) > index-padding and float(photo['index']) < index+padding:
			thisYear['photos'].append({'index': photo['index'], 'filename': photo['filename']})

	out['photo-years'].append(thisYear)

with open(str(address)+'.json','w') as outFile:
	json.dump(out,outFile)
			