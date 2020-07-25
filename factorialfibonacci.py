from time import asctime
x = 25

def gettime():
    from datetime import datetime
    
    dt = datetime.now()
    return dt.microsecond

def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num >= 2:
        return num * factorial(num-1)
    else:
        return abs(num * factorial(num+1)) * -1
    
    
def fibonacci(num):
    x1 = 0
    x2 = 1
    if num < 0: return "N/A"
    elif num == 0: return 0
    elif num == 1 or num == 2: return 1
    else:
        for i in range (2, num):
            x3 = x1 + x2
            x1 = x2
            x2 = x3
            x3 = x1 + x2
        return x3
#print(asctime(
def fibonaccirecur(num):
    if num < 0: return "N/A"
    elif num == 0: return 0
    elif num == 1 or num == 2: return 1
    else:
        sum = fibonaccirecur(num-1) + fibonaccirecur(num-2)
        return sum

#print(asctime(
cache = dict()
cache[1] = 1
cache[2] = 1
def fibonaccirecurCached(num):
    if num < 0: return "N/A"
    elif num == 0: return 0
    elif num == 1 or num == 2: return cache[num]
    else:
        if ((num-1) in cache.keys()):
            x1 = cache[num-1]
        else:
            x1=fibonaccirecurCached(num-1)
            cache[num-1] = x1

        if ((num-2) in cache.keys()):
            x2 = cache[num-2]
        else:
            x2=fibonaccirecurCached(num-2)
            cache[num-2] = x2
            
 
        sum = x1 + x2
        cache[num] = sum
        return sum
    
    
i1 = gettime()
y = fibonacci(x)
i2 = gettime()
i3 = gettime()
y2 = fibonaccirecur(x)
i4 = gettime()
i5 = gettime()
y3 = fibonaccirecurCached(x)
i6 = gettime()
print(str(fibonacci(x)) + ' took ' + str(i2-i1) + ' microseconds.')
print(str(fibonaccirecur(x)) + ' took ' + str(i4-i3) + ' microseconds.')
print(str(fibonaccirecurCached(x)) + ' took ' + str(i6-i5) + ' microseconds.')