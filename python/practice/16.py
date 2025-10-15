l = [1, 2, 3, 4]
done = False

def check(num, l):
    cows = 0
    bulls = 0
    for i in range(len(l)):
        if l[i] == num[i]:
            cows += 1
    print(cows, "cows,", bulls, "bulls")

while not done:
    num = int(input("Guess the code "))
    num = num.split("")
    check(num, l)
    
