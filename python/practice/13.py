import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def getOverlap(a, b):
  c = []
  d = []
  
  for x in range(len(a)):
    for y in range(len(b)):
      if a[x] == b[y]:
        c.append(a[x])
      
  for i in set(c):
    d.append(i)
  print(d)
  
getOverlap(a, b)

'''aLen = random.randrange(0, 10)
bLen = random.randrange(0, 10)
for i in range(len(a)):
  a.append(random.randrange(5))
for i in range(len(b)):
  b.append(random.randrange(5))'''

