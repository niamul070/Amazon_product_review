#!/usr/bin/python
import sys

inFile = open(sys.argv[1], 'r')#test data file
inFile1 = open(sys.argv[2], 'r') #attribute file
oFile1 = open(sys.argv[3], 'w') #out put the dictionary values
oFile2 = open(sys.argv[4], 'w') #out put the dictionary keys


#take the first line which contains the attributes from trianing data

attrToKeep = [line.strip() for line in inFile1]
inFile1.close()

#parse the test file
dataPoints = []

for line in inFile:
  tempDict = {}
  s_line = line.rstrip()
  part = s_line.split(' ')
  for each in part:
    key = each.split(":")[0]
    value = each.split(":")[1]
    tempDict[key] = value
  dataPoints.append(tempDict)

print "total number of data points:", len(dataPoints)
inFile.close()

merged_data_points = {
}

for data_point in dataPoints:
    for k, v in data_point.items():
        if k not in merged_data_points:
            merged_data_points[k] = []
        merged_data_points[k].append(v)

print "total number of attributes before pruning: ", len(merged_data_points)

#parse which attribute to keep and put in tempDict
tempDict = {}
for i in range(len(attrToKeep)):
  if attrToKeep[i] in merged_data_points:
    tempDict[attrToKeep[i]] = merged_data_points[attrToKeep[i]]

print "total number of attributes after pruning: ", len(tempDict)


for k in tempDict:
    out1 = '{0}\n'.format(tempDict[k] )
    out2 = '{0}\n'.format(k)
    oFile1.write(out1)
    oFile2.write(out2)

oFile1.close()
oFile2.close()
