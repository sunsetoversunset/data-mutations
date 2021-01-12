#!/usr/bin/env python3


import fiona
import shapely.geometry
import csv
import sys
import os

debug = False

def process(f):


	inFile = f
	outFileN = os.path.basename(f).split('.')[0] + "-n.csv"
	outFileS = os.path.basename(f).split('.')[0] + "-s.csv"


	with fiona.open(inFile) as pointsSrc:

		maskSrc = fiona.open('../Street Data/sunset-buffered.gpkg')

		for s in maskSrc:
			# print ("Shape here")
			maskGeom = shapely.geometry.shape(s['geometry'])

		lineSrc = fiona.open('../Street Data/sunset-single-line.gpkg')

		for s in lineSrc:
			# print ("Shape here")
			lineGeom = shapely.geometry.shape(s['geometry'])

		with open(outFileN,'w') as outFileN:

			with open(outFileS,'w') as outFileS:
			
				writerN = csv.DictWriter(outFileN, fieldnames=['filename','index'])
				writerN.writeheader()

				writerS = csv.DictWriter(outFileS, fieldnames=['filename','index'])
				writerS.writeheader()

				for s in pointsSrc:
					if s['geometry'] == None: continue

					p = shapely.geometry.shape(s['geometry'])

					if p.within(maskGeom):

						t = {}
						
						idx = lineGeom.project(p,normalized=True)
						
						t['filename'] = s['properties']['filename'].split('/')[-1]
						# t['bearing'] = s['properties']['bearing']
						t['index'] = idx

						if s['properties']['bearing'] > 180: 

							writerS.writerow(t)
						else:
							writerN.writerow(t)


for file in sys.argv[1:]:
	process(file)
