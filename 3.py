import math

num = 600851475143  
def l(num):
    val = 0
    for g in range(1,int(math.sqrt(num))):
        if num%g == 0 and g > val:
            val = g
    print(val)
    val = num//val
    if val == num:
        return True
    else:
        return val

while l(num) != True:
    num = l(num)
    print(num)
else:
    print(l(num))