import math
x=math.pi/6
y=0.0
n=1
p=0.0
ind=1.0
while(True):
    p=y
    
    y+=ind * (math.pow(x, n)/math.factorial(n))
    
    if abs(y-p) < 0.00001:
        break
    n=n+2
    ind*=-1
print(y)      