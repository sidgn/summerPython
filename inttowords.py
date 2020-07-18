num1 = 999999
#dig = list(str(num1))
#print(dig)

def blankzero(x):
    if x == 'zero':
        return ''
    return x

def gettext(num):
    #print ('num:' + str(num))
    dig = list(str(num))
    numberwords = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    if num in numberwords.keys():
        return numberwords[num]
    elif len(dig) == 2:
        return numberwords[int(dig[0]) * 10] + "-"+ numberwords[int(dig[1])]
    elif len(dig) == 3:
        x1=''
        if int(dig[1]) == 0:
            x1=''
        else:
            x1=numberwords[int(dig[1]) * 10]
        #return numberwords[int(dig[0]) * 100] + numberwords[int(dig[1]) * 10] + "-"+ numberwords[int(dig[2])]
        return numberwords[int(dig[0])] + " hundred " + blankzero(numberwords[int(dig[1]) * 10]) + " " + blankzero(numberwords[int(dig[2])])
    elif len(dig) == 4:
        x1=''
        x2=''
        if int(dig[2]) == 0:
            x1=''
        if int(dig[1]) == 0:
            x2 = ''
        else:
            x1=numberwords[int(dig[2]) * 10]
            x2=numberwords[int(dig[1])] + " hundred "
        
        return numberwords[int(dig[0])] + " thousand " + x2 + blankzero(numberwords[int(dig[2]) * 10]) + " " + blankzero(numberwords[int(dig[3])])
    elif len(dig) == 5:
        x1=''
        x2=''
        x3 ="".join(dig[0:2])
        if int(dig[3]) == 0:
            x1=''
        if int(dig[2]) == 0:
            x2 = ''
        else:
            x1=numberwords[int(dig[3]) * 10]
            x2=numberwords[int(dig[2])] + " hundred "
        #return numberwords[int(x3)] + " thousand " + x2 + blankzero(numberwords[int(dig[3]) * 10]) + " " + blankzero(numberwords[int(dig[4])])
        return gettext(int(x3)) + " thousand " + x2 + blankzero(numberwords[int(dig[3]) * 10]) + " " + blankzero(numberwords[int(dig[4])])
    elif len(dig) == 6:
        x1=''
        x2=''
        x3 ="".join(dig[0:3])
        if int(dig[4]) == 0:
            x1=''
        if int(dig[3]) == 0:
            x2 = ''
        else:
            x1=numberwords[int(dig[4]) * 10]
            x2=numberwords[int(dig[3])] + " hundred "
        #return gettext(int(x3)) + " thousand " + x2 + blankzero(numberwords[int(dig[4]) * 10]) + " " + blankzero(numberwords[int(dig[5])])
        return gettext(int(x3)) + " thousand " + x2 + blankzero(numberwords[int(dig[4]) * 10]) + " " + blankzero(numberwords[int(dig[5])])

print(gettext(num1))
        