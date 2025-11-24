import math

num = 2+3+5+7

def isprime(j):
    for k in range(2,int(math.sqrt(j))+1):
        if j%k==0:
            return False
    return True

for i in range(3,2000000,2):
    if i%5!=0 and i%3!=0 and i%7!=0:
        if isprime(i):
            num += i

print(num)