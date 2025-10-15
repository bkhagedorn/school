import random
a = []
b = []
aLen = random.randrange(3, 11)
for i in range(aLen):
    a.append(random.randrange(1, 101))

def ffsg(a, b):
    b.append(a[0])
    b.append(a[-1])
    print(b)

ffsg(a, b)
    
