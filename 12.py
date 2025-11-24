import math

def num(a):
    k = 0
    for t in range(1,int(math.sqrt(a))):
        if a%t == 0:
            k += 2
    return k

n = 100
while num(n*(n+1)//2) < 500:
    n += 1
else:
    print(n*(n+1)//2)
