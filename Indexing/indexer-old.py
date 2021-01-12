import fiona
import shapely.geometry
import csv


inFile = '../Data Exports/Converted to GeoJSON/2012m2_ref33_oy0.json-flattened.json'

outDict = []

with fiona.open(inFile) as pointsSrc:

	maskSrc = fiona.open('../Street Data/sunset-buffered.gpkg')

	for s in maskSrc:
		# print ("Shape here")
		maskGeom = shapely.geometry.shape(s['geometry'])

	lineSrc = fiona.open('../Street Data/sunset-single-line.gpkg')

	for s in lineSrc:
		# print ("Shape here")
		lineGeom = shapely.geometry.shape(s['geometry'])

	with fiona.collection('test-out.geojson','w','GeoJSON',{'geometry': 'Point', 'properties': {'filename': 'str', 'bearing': 'str', 'index': 'float'}}) as outFile:


		for s in pointsSrc:
			if s['geometry'] == None: continue
			if s['properties']['bearing'] > 180: continue

			p = shapely.geometry.shape(s['geometry'])

			if p.within(maskGeom):

				t = {'properties': {}, 'geometry': {}}
				
				idx = lineGeom.project(p,normalized=True)
				
				t['properties']['filename'] = s['properties']['filename']
				t['properties']['bearing'] = s['properties']['bearing']
				t['properties']['index'] = idx
				t['geometry'] = shapely.geometry.mapping(p)

				outFile.write(t)



# with open('tmp-csv.csv','w') as outFile:
# 	writer = csv.DictWriter(outFile, fieldnames=['filename','bearing','index','coordinates'])
# 	for row in outDict:
# 		writer.writerow(row)

