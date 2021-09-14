import csv

file = open("Descriptive104/SOCR-HeightWeight.csv", newline="")
reader = csv.reader(file)
fileData = list(reader)
#print(fileData)
fileData.pop(0)
newData = []
for i in range(len(fileData)) :
    num = fileData[i][2]
    newData.append(float(num))

n = len(newData)
newData.sort()

if n%2 ==0 :
    median1 = float(newData[n//2])
    median2 = float(newData[n//2 -1])
    Median= (median1+median2)/2

else :
    Median = newData[n//2]

print(Median)