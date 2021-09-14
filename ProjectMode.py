import csv
from typing import Counter

file = open("Descriptive104/SOCR-HeightWeight.csv", newline="")
reader = csv.reader(file)
fileData = list(reader)
#print(fileData)
fileData.pop(0)
newData = []
for i in range(len(fileData)) :
    num = fileData[i][2]
    newData.append(float(num))

data = Counter(newData)
modeDataForRange = {
    '75-85' : 0,
    '85-95' : 0,
    '95-105' : 0,
    '105-115' : 0,
    '115-125' : 0,
    '125-135' : 0,
    '135-145' : 0,
    '145-155' : 0,
    '155-165' : 0,
    '165-175' : 0, 
}

for weight, occurence in data.items() :
    if 75<float(weight)<85 :
        modeDataForRange['75-85'] += occurence
    elif 85<float(weight)<95 :
        modeDataForRange['85-95'] += occurence
    elif 95<float(weight)<105 :
        modeDataForRange['95-105'] += occurence
    elif 105<float(weight)<115 :
        modeDataForRange['105-115'] += occurence
    elif 115<float(weight)<125 :
        modeDataForRange['115-125'] += occurence
    elif 125<float(weight)<135 :
        modeDataForRange['125-135'] += occurence
    elif 135<float(weight)<145 :
        modeDataForRange['135-145'] += occurence
    elif 145<float(weight)<155 :
        modeDataForRange['145-155'] += occurence
    elif 155<float(weight)<165 :
        modeDataForRange['155-165'] += occurence
    elif 165<float(weight)<175 :
        modeDataForRange['165-175'] += occurence


print(modeDataForRange)

modeRange,modeOccurence = 0,0
for range,occurence in modeDataForRange.items() :
    if occurence>modeOccurence :
        modeRange,modeOccurence = [int(range.split('-')[0]),int(range.split('-')[1]) ], occurence

Mode = float((modeRange[0] + modeRange[1])/2)
print(Mode)