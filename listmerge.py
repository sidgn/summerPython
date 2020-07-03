list1 = [1, 2, 3]
#list2 = []
list2 = [7, 8, 9, 11, 12]
list3 = []
i = 0
x1=0
while True:
    if i >= len(list1) and i >= len(list2): break
    if i >= len(list1):
        x1=0    
    else: list3.append(list1[i])
    if i >= len(list2):
        x1=0
    else: list3.append(list2[i])
    i += 1
print(list3)