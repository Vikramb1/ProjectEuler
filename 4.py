large = 0
for i in range(100,1000):
    for t in range(100,1000):
        if t*i > large and str(t*i) == str(t*i)[::-1]:
            print(t,i)
            large = t*i
            
print(large)


