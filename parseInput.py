#!/usr/bin/python
import sys

inFile = open(sys.argv[1], 'r')
outFile = open(sys.argv[2], 'w')
globalDict = {}
labelList = []


for line in inFile:
  tempDict = {}
  s_line = line.rstrip()
  part = s_line.split(' ')
  for each in part:
    key = each.split(":")[0]
    value = each.split(":")[1]
    if not key == "#label#":
      tempDict[key] = value
      if key not in globalDict:
        globalDict[key] = 0
    else:
      labelList.append(value)
  #print tempDict
#creaetd a global dictionary of words
outFile.write(str(globalDict))
print labelList
inFile.close()
outFile.close()
