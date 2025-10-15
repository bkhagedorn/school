done = False
p1 = ""
p2 = ""
d = ""

while not done:
  p1 = input("Rock, paper, or scissors? ").lower().strip()
  p2 = input("Rock, paper, or scissors? ").lower().strip()
  
  if p1 == "rock":
    if p2 == "rock":
      print("Tie")
    if p2 == "scissors":
      print("P1 Wins!")
    if p2 == "paper":
      print("P2 Wins!")
  
  if p1 == "paper":
    if p2 == "paper":
      print("Tie")
    elif p2 == "rock":
      print("P1 Wins!")
    if p2 == "scissors":
      print("P2 Wins!")
  
  if p1 == "scissors":
    if p2 == "scissors":
      print("Tie")
    elif p2 == "paper":
      print("P1 Wins!")
    if p2 == "rock":
      print("P2 Wins!")
      
  d = input("Do you want to play again? (Y/N) ").lower().strip()
  if d == "n":
    done = True