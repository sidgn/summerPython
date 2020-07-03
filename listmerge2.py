list2 = [1, 2, 5, 7, 6]
list1 = [1, 2, 11, 13]
thisdict = dict()
i = 0
x1 = 0
while True:
    if i >= len(list1) and i >= len(list2): break
    if i >= len(list1):
        x1 = 0    
    elif list1[i] in thisdict: thisdict[list1[i]] += 1
    else: thisdict[list1[i]] = 1
    if i >= len(list2):
        x1 = 0    
    elif list2[i] in thisdict: thisdict[list2[i]] += 1
    else: thisdict[list2[i]] = 1
    i += 1
print(thisdict.keys())