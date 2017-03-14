#!/usr/bin/python
import sys

inFile = open(sys.argv[1], 'r')#train data file
oFile1 = open(sys.argv[2], 'w') #out put the dictionary values
#oFile2 = open(sys.argv[3], 'w') #out put the dictionary keys / this is the attributes after pruning


#parse the train file
dataPoints = []

def notToKeep(s):
  l = s.split(' ')
  zeroCount = 0
  for i in l:
      if eval(i) == 0:
        zeroCount += 1
  threshold = 95.0 * len(dataPoints)/100.0
  if zeroCount > threshold:
    return 1 #do not keep this column
  else:
    return 0

for line in inFile:
  tempDict = {}
  s_line = line.rstrip()
  part = s_line.split(' ')
  for each in part:
    key = each.split(":")[0]
    value = each.split(":")[1]
    if not key == "#label#":
      tempDict[key] = value
      #c += 1
    #else:
    #  labelList.append(value)
  dataPoints.append(tempDict)

keys = sorted(set.union(*(set(dp) for dp in dataPoints)))
print "Hi"
merged_data_points = []
for i, datapoint in enumerate(dataPoints):
    out = '{}'.format(' '.join(str(datapoint.get(k, 0)) for k in keys))
    merged_data_points.append(out)
#oFile1.write(str(merged_data_points))
oFile1.close()
print "total number of attributes before pruning: ", len(merged_data_points)
'''
# compute the frequency
listTokeep = []
for k in merged_data_points:
  if not notToKeep(k): #keep this
    listTokeep.append(k)

print "total number of attributes after pruning: ", len(listTokeep)
#print the dictionary with the required keys

#write to files
finalList = [[]]
finalList = [[0 for i in range(len(listTokeep))] for j in range(len(dataPoints))]

i = 0
for k, v in listTokeep.items():
  col = i
  i+=1
  for j in range(len(v)):
    #print v, j, v[j]
    row = eval(v[j].split('_')[1])
    val = eval(v[j].split('_')[0])
    finalList[row][col] = val

for k in listTokeep:
    #out1 = '{0}\n'.format(listTokeep[k] )
    out2 = '{0}\n'.format(k)
    oFile2.write(out2)
for each in finalList:
  out = str(each) + '\n'
  oFile1.write(out)

oFile1.close()
oFile2.close()'''
