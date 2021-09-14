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
sum = 0
for i in newData :
    sum += i

Mean = sum/n
print(Mean)
