#!/usr/bin/env python3


import fiona
import shapely.geometry
import csv
import sys
import os

def process(f):

	inFile = f
	outFileN = "addresses-n.csv"
	outFileS = "addresses-s.csv"

	with fiona.open(inFile) as pointsSrc:

		lineSrc = fiona.open('../Street Data/sunset-single-line.gpkg')

		for s in lineSrc:
			# print ("Shape here")
			lineGeom = shapely.geometry.shape(s['geometry'])

		with open(outFileN,'w') as outFileN:
			with open(outFileS,'w') as outFileS:
	
				writerN = csv.DictWriter(outFileN, fieldnames=['address','index'])
				writerN.writeheader()

				writerS = csv.DictWriter(outFileS, fieldnames=['address','index'])
				writerS.writeheader()

				for s in pointsSrc:
					if s['geometry'] == None: continue

					p = shapely.geometry.shape(s['geometry'])

					t = {}
					
					idx = lineGeom.project(p,normalized=True)
					
					t['address'] = str(s['properties']['Number'])
					# t['bearing'] = s['properties']['bearing']
					t['index'] = idx

					if s['properties']['Number'] % 2 == 0:
						writerS.writerow(t)
					else:
						writerN.writerow(t)


for file in sys.argv[1:]:
	process(file)
