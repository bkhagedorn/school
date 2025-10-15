name = input("Enter your name ")
age = int(input("Enter your age "))
num = int(input("Enter another number "))

for i in range(num):
  print(name + ", you will turn 100 in " + str(100 - age) + " years.")