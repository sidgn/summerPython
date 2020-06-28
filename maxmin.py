lst1 = [2,5,23,5,3,5,1,29,12]
x = None
def max():
    for i in range(0, len(lst1)-1):
        if i == 0: x = lst1[i]
        elif lst1[i] > lst1[i-1]: x = lst1[i]
        else: continue
    return x
def min(): 
    for i in range(0, len(lst1)-1):
        if i == 0: x = lst1[i]
        elif lst1[i] < lst1[i-1]: x = lst1[i]
        else: continue
    return x
def mean():
    sum = 0
    for number in lst1:
        sum += number
    mean = sum / len(lst1)
    return mean
def median():
    '''y = 0
    for i in range(1, len(lst1)):
        if lst1[i] < lst1[i-1]:
            y = lst1[i]
            lst1[i] = lst1[i-1]
            lst1[i-1] = y
        else: continue'''
    lst1.sort()
    if len(lst1) % 2 == 0:
        med = (lst1[len(lst1)/2] + lst1[len(lst1)/2 - 1]) / 2
    else: med = lst1[int((len(lst1)/2)-0.5)]
    return med
def mode():
    numbercnt = dict()
    for i in lst1:
        if i in numbercnt:
            numbercnt[i] += 1
        else:
            numbercnt[i] = 1
    
    modevalue=-1
    modekey=""
    for key in numbercnt.keys():
        v1 = numbercnt[key]
        if v1 > modevalue:
            modevalue = v1
            modekey=key
    return modekey
print(mode())
        
            