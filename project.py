import csv
from collections import Counter

with open('data1.csv', newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    someName=file_data[i][1]
    new_data.append(someName)

data=Counter(new_data)
modedata_forRange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurence in data.items():
    if 50<float(height)<60:
        modedata_forRange["50-60"]+=occurence
    elif 60<float(height)<70:
        modedata_forRange["60-70"]+=occurence
    elif 70<float(height)<80:
        modedata_forRange["70-80"]+=occurence

modeRange,modeOccurence=0,0
for range,occurence in modedata_forRange.items():
    if occurence > modeOccurence:
        modeRange,modeOccurence=[int(range.split("-")[0]),int (range.split("-")[1])],occurence

mode=float((modeRange[0]+modeRange[1])/2)


n=len(new_data)
new_data.sort()

if n % 2 == 0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2

else:
    median=new_data[n//2]

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    someName=file_data[i][1]
    new_data.append(float(someName))

n = len(new_data)
total = 0

for x in new_data:
    total+=x

mean=total/n
print("The mean is... "+str(mean))
print("The median is... "+str(median))
print(f"Mode is -> {mode:2f}")