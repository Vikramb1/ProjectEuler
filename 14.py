t = [0,0]
for y in range(1,1000000):
    v = y
    num = 1
    while v != 1:
        num += 1
        if v%2==0:
            v = v//2
        else:
            v = 3*v+1
    else:
        if num > t[0]:
            t[0] = num
            t[1] = y

print(t) 