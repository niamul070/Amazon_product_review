#!/usr/bin/python
import sys

inFile = open(sys.argv[1], 'r')#test data file
inFile1 = open(sys.argv[2], 'r') #attribute file
oFile1 = open(sys.argv[3], 'w') #out put test matrix
oFile2 = open(sys.argv[4], 'w') #out put the attributes


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

merged_data_points = {}
i = 0
for data_point in dataPoints:
    i=i+1
    for k, v in data_point.items():
        if k not in merged_data_points:
            merged_data_points[k] = []
        v1 = str(v)+"_" + str(i-1) #keeping the document data
        merged_data_points[k].append(v1)
print "total number of attributes before pruning: ", len(merged_data_points)
#sorted(merged_data_points)
#parse which attribute to keep and put in tempDict
tempDict = {}
for i in range(len(attrToKeep)):
  if attrToKeep[i] in merged_data_points:
    tempList = []
    tempList.append([1])
    tempList.append(merged_data_points[attrToKeep[i]])
    tempDict[attrToKeep[i]] = tempList

print "total number of attributes after pruning: ", len(tempDict)

finalList = [[]]
finalList = [[0 for i in range(len(tempDict))] for j in range(len(dataPoints))]

i = 0
for k, v in tempDict.items():
  col = v[0]
  i+=1
  for j in range(1, len(v)):
    #print v, j, v[j]
    row = eval(v[j].split('_')[1])
    val = eval(v[j].split('_')[0])
    finalList[row][col] = val
print tempDict.keys()
for k in tempDict:
    out2 = '{0}\n'.format(k)
    oFile2.write(out2)

for each in finalList:
  out = str(each) + '\n'
  oFile1.write(out)

oFile1.close()
oFile2.close()
