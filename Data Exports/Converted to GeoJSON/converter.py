#!/usr/bin/env python3

import json
import sys
import os


def processFile(file):

	outData = {
	"type": "FeatureCollection",
	"features": []
	}

	outFile = os.path.basename(file) + "-flattened.json"

	with open(file,'r') as inFile:
		record = json.load(inFile)

		for r in record:
			for f in r["features"]:
				outData["features"].append(f)

	with open(outFile, 'w') as outPipe:
		json.dump(outData, outPipe)


for file in sys.argv[1:]:
	processFile(file)


