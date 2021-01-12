from sys import argv
import csv

infile = argv[1]

with open('./map2-brainfood_ids_amended.csv','r') as crosswalkFile:

    crosswalkDict = {}
    for line in crosswalkFile:
        split = line.split(',')
        crosswalkDict[split[0]] = split[1][:-1]
    
    
    output = []
    
    with open(infile,'r') as sourceFile:
        reader = csv.DictReader(sourceFile)

        for row in reader:
            newIdentifier = crosswalkDict[row['filename'].split('_')[-1]]
            output.append([newIdentifier,row['index']])

    
    with open('./reidentified/{}'.format(infile), 'w+') as outFile:
        outFile.write('identifier,index\n')
        for row in output:
            outFile.write('{},{}\n'.format(row[0],row[1]))




