x = 5
def factorial():
    a = 1
    if x == 0 or x == 1:
        a = 1
    else:
        for i in range(1, abs(x)+1):
            a *= i
        if x < 0:
            a *= -1
    print(a)
def fibonacci():
    seq = [0, 1]
    for i in range (2, x):
        seq.append(seq[i-1]+seq[i-2])
    print(seq)
fibonacci()