def reverse(word):
  string = word.split()
  string = string[::-1]
  string = " ".join(string)
  print(string)
  
word = input("Enter a sentence ")
reverse(word)