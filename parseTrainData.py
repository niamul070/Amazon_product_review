#!/usr/bin/python
import sys

inFile = open(sys.argv[1], 'r')#train data file
oFile1 = open(sys.argv[2], 'w') #out put the dictionary values
oFile2 = open(sys.argv[3], 'w') #out put the dictionary keys / this is the attributes after pruning


#parse the train file
dataPoints = []

def notToKeep(s):
  zeroCount = len(dataPoints) - len(s)
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
print "total number of data points:", len(dataPoints)

merged_data_points = {
}

inFile.close()

#build the train dict
for data_point in dataPoints:
    for k, v in data_point.items():
        if k not in merged_data_points:
            merged_data_points[k] = []
        merged_data_points[k].append(v)
print "total number of attributes before pruning: ", len(merged_data_points)

# compute the frequency
listTokeep = {}
for k in merged_data_points:
  if not notToKeep(merged_data_points[k]): #keep this
    listTokeep[k] = merged_data_points[k]

#print the dictionary with the required keys
print "total number of attributes after pruning: ", len(listTokeep)

#write to files
for k in listTokeep:
    out1 = '{0}\n'.format(listTokeep[k] )
    out2 = '{0}\n'.format(k)
    oFile1.write(out1)
    oFile2.write(out2)

oFile1.close()
oFile2.close()


'''#!/usr/bin/python
#python3 parseInput.py train1.dat labelTrain1.dat
import sys

inPrep = open("preposition.txt")
inFile = open(sys.argv[1], 'r')
oFile = open(sys.argv[2], 'w')
dataPoints = []
labelList = []
prepList = []
#parse input file
for line in inPrep:
  s_line = line.rstrip()
  part = line.split()
  for each in part:
    prepList.append(each)
inPrep.close()
#print(prepList)

def usefulWord(key):
  if '_' in key:
      part = key.split('_')
      if (not(part[0] in prepList) and not(part[1] in prepList)):
        return 1
  else:
    if not(key in prepList):
      return 1

c =0

for line in inFile:
  tempDict = {}
  s_line = line.rstrip()
  part = s_line.split(' ')
  for each in part:
    key = each.split(":")[0]
    value = each.split(":")[1]
    if not key == "#label#":
     #if usefulWord(key):
      tempDict[key] = value
      #c += 1
    else:
      labelList.append(value)
  dataPoints.append(tempDict)
  #print ("tempDict" , (len(tempDict)))
for item in labelList:
  oFile.write("%s\n" %item)

# get all the keys ever seen
keys = sorted(set.union(*(set(dp) for dp in dataPoints)))
print (len(keys))
count = 0

with open("outFileMatrixTrainFS3.dat", "w") as outFile:
    # write the header
    #outFile.write("{}\n".format(' '.join([" "] + keys)))
    # loop over each point, getting the values in order (or 0 if they're absent)
    for i, datapoint in enumerate(dataPoints):
        #out = '{} {}\n'.format(i, ' '.join(str(datapoint.get(k, 0)) for k in keys))
        out = '{}\n'.format(' '.join(str(datapoint.get(k, 0)) for k in keys))
        count +=1
        outFile.write(out)
print (count)
inFile.close()
outFile.close()
oFile.close()'''


