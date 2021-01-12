#!/usr/bin/env python3


import fiona
import shapely.geometry
import csv
import sys
import os

debug = False

def process(f):


	inFile = f
	outFileN = "intersections-n.csv"
	outFileS = "intersections-s.csv"


	with fiona.open(inFile) as pointsSrc:

		lineSrc = fiona.open('../Street Data/sunset-single-line.gpkg')

		for s in lineSrc:
			# print ("Shape here")
			lineGeom = shapely.geometry.shape(s['geometry'])

		with open(outFileN,'w') as outFileN:

			with open(outFileS,'w') as outFileS:
			
				writerN = csv.DictWriter(outFileN, fieldnames=['intersection','index'])
				writerN.writeheader()

				writerS = csv.DictWriter(outFileS, fieldnames=['intersection','index'])
				writerS.writeheader()

				for s in pointsSrc:
					if s['geometry'] == None: continue

					p = shapely.geometry.shape(s['geometry'])

					t = {}
					
					idx = lineGeom.project(p,normalized=True)
					
					t['intersection'] = s['properties']['name']
					# t['bearing'] = s['properties']['bearing']
					t['index'] = idx

					if s['properties']['south']: 

						writerS.writerow(t)
					
					if s['properties']['north']:

						writerN.writerow(t)


for file in sys.argv[1:]:
	process(file)
