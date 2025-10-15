num = int(input("Enter a number "))
isPrime = False

for i in range(2, num):
    if num % i == 0:
        isPrime = True

if isPrime:
    print("Not Prime")
else:
    print("Prime")
