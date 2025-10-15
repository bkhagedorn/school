a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
check = int(input("Enter a number "))

for i in range(len(a)):
  if a[i] < check:
    b.append(a[i])
print(b)