a = 1
b = 1
sum = 0
while a + b < 4e6:
    n = a+b
    a = b
    b = n
    if b%2==0:
        sum+=b

print(sum)