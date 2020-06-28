import math
i = 2354
# Why mod is being done outside?
lst1 = list()
while i > 0: # why check m
    m = i % 10
    i = (i-m)/10
    lst1.append(int(m))
    #print(int(m),end='')
#for x in range(0, len(lst1)):
sum = 0
for x in range(0, len(lst1)):
    #sum += lst1[-x]
    power1=len(lst1)-1-x
    value=lst1[x]
    sum = sum + int(value*math.pow(10, power1))
print(sum)