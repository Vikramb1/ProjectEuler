import math

def isprime(j):
    for k in range(2,int(math.sqrt(j))+1):
        if j%k==0:
            return False
    return True

count = 2
num = 0
while num < 10001:
    if isprime(count):
        num += 1
    count += 1

print(count)
