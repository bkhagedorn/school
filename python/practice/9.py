import random

num = random.randrange(1, 10)
guess = 0
done = False

while not done:
  a = input("Guess the number")
  guess += 1
  if a == "exit":
    done = True
    print("The number was " + str(num) + ".")
  elif int(a) == num:
    print("Good job! The number was " + str(num) + ".")
    print("It took " + str(guess) + " guesses.")
    print("")
    num = random.randrange(1, 10)
    guess = 0