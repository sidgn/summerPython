import math
num = 101
def tobinary():
    a = num
    bindig = []
    while a > 0:
        if a % 2 < 1:
            #bindig.insert(len(bindig), 0)
            bindig.insert(0, 0)
        else:
            bindig.insert(0, 1)
        a = int(a/2)
        print (a)
    print(bindig)

def toint():
    a = 0
    bindig = list(str(num))
    for i in range (0, len(bindig)):
        a += int(bindig[i]) * int(math.pow(2, i))
    print(a)
toint()