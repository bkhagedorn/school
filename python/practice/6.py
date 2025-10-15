check = input("Enter a word ")

if check == check[::-1]:
    print(check, "is a palindrome")
else:
    print(check, "is not a palindrome")

