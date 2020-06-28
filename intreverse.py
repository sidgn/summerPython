number = 2354
strnumber = str(number)
digitlist = list()
for x in range (1, len(strnumber) +1):
    digitlist.append(strnumber[-x])
for y in range (0, len(digitlist)):
    print(digitlist[y], end='')
