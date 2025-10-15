def fibonacci(length):
  a = []
  
  for i in range(length):
    if i == 0 or i == 1:
      a.append(1)
    else:
      a.append(a[i-1] + a[i-2])
  print(a)

length = int(input("How many fibonacci number do you want?"))
fibonacci(length)