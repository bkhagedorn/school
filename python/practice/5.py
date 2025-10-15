import random
a = []
b = []
c = []
d = []

aLen = random.randrange(0, 10)
bLen = random.randrange(0, 10)
for i in range(aLen):
  a.append(random.randrange(5))
for i in range(bLen):
  b.append(random.randrange(5))

for x in range(len(a)):
  for y in range(len(b)):
    if a[x] == b[y]:
      c.append(a[x])
      
for i in set(c):
  d.append(i)
print(d)