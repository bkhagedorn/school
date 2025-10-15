#1 sum
def sumPrint(a, b):
    result = a + b
    print("The sum is:")
    print(result)

#2 difference
def difPrint(a, b):
    result = a - b
    print("The difference is:")
    print(result)

#3 product
def proPrint(a, b):
    result = a * b
    print("The product is:")
    print(result)

#4 quotient
def quoPrint(a, b):
    result = a / b
    print("The quotient is:")
    print(result)

#5 average
def avePrint(a, b, c, d):
    result = (a + b + c + d) / 4
    print("The average is:")
    print(result)

done = False
while not done:
    print("Which function do you want to call? (Sum, difference, product, quotient, and average)")
    choice = input().lower().strip()
    a = int(input("Enter first value "))
    b = int(input("Enter second value "))
    if choice == "average":
        c = int(input("Enter third value "))
        d = int(input("Enter fourth value "))
        
    if choice == "sum":
        sumPrint(a, b)
        print()
    elif choice == "difference":
        difPrint(a, b)
        print()
    elif choice == "product":
        proPrint(a, b)
        print()
    elif choice == "quotient":
        quoPrint(a, b)
        print()
    elif choice == "average":
        avePrint(a, b, c, d)
        print()
        
