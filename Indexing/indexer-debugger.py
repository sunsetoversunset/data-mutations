#!/usr/bin/env python3


import fiona
import shapely.geometry
import csv
import sys
import os


def process(lat,lng):



	maskSrc = fiona.open('../Street Data/sunset-buffered.gpkg')

	for s in maskSrc:
		# print ("Shape here")
		maskGeom = shapely.geometry.shape(s['geometry'])

	lineSrc = fiona.open('../Street Data/sunset-single-line.gpkg')

	for s in lineSrc:
		# print ("Shape here")
		lineGeom = shapely.geometry.shape(s['geometry'])


	p = shapely.geometry.Point(lng,lat)

	if p.within(maskGeom):

		idx = lineGeom.project(p,normalized=True)
					
		print(idx)

	else:

		print("not in buffer")



process(34.098072, -118.361564)
