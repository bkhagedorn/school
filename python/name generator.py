days = []
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
dwte = 1
firstName = ""
lastName = ""
dayInput = 0
monthInput = ""
for i in range(31):
  days.append(dwte)
  dwte += 1

def findFirstName(dayInput):
  if dayInput == days[0]:
    firstName = "Active"
  elif dayInput == days[1]:
    firstName = "Affectionate"
  elif dayInput == days[2]:
    firstName = "Agile"
  elif dayInput == days[3]:
    firstName = "Amusing"
  elif dayInput == days[4]:
    firstName = "Anxious"
  elif dayInput == days[5]:
    firstName = "Beautiful"
  elif dayInput == days[6]:
    firstName = "Beloved"
  elif dayInput == days[7]:
    firstName = "Best"
  elif dayInput == days[8]:
    firstName = "Big"
  elif dayInput == days[9]:
    firstName = "Calm"
  elif dayInput == days[10]:
    firstName = "Chill"
  elif dayInput == days[11]:
    firstName = "Chubby"
  elif dayInput == days[12]:
    firstName = "Clumsy"
  elif dayInput == days[13]:
    firstName = "Crazy"
  elif dayInput == days[14]:
    firstName = "Delicate"
  elif dayInput == days[15]:
    firstName = "Dominant"
  elif dayInput == days[16]:
    firstName = "Fluffy"
  elif dayInput == days[17]:
    firstName = "Gentle"
  elif dayInput == days[18]:
    firstName = "Giant"
  elif dayInput == days[19]:
    firstName = "Goofy"
  elif dayInput == days[20]:
    firstName = "Grumpy"
  elif dayInput == days[21]:
    firstName = "Intelligent"
  elif dayInput == days[22]:
    firstName = "Jolly"
  elif dayInput == days[23]:
    firstName = "Joyous"
  elif dayInput == days[24]:
    firstName = "Lazy"
  elif dayInput == days[25]:
    firstName = "Mischevious"
  elif dayInput == days[26]:
    firstName = "Silly"
  elif dayInput == days[27]:
    firstName = "Muscular"
  elif dayInput == days[28]:
    firstName = "Naughty"
  elif dayInput == days[29]:
    firstName = "Pouncing"
  elif dayInput == days[30]:
    firstName = "Quirky"
  return firstName

def findLastName(monthInput):
  if monthInput == "january":
    lastName = "Sphynx"
  elif monthInput == "february":
    lastName = "Ragdoll"
  elif monthInput == "march":
    lastName = "Bombay"
  elif monthInput == "april":
    lastName = "Calico"
  elif monthInput == "may":
    lastName = "Stupid idiot"
  elif monthInput == "june":
    lastName = "Bermese"
  elif monthInput == "july":
    lastName = "Billy"
  elif monthInput == "august":
    lastName = "Boy"
  elif monthInput == "september":
    lastName = "Girl"
  elif monthInput == "october":
    lastName = "Ford F150"
  elif monthInput == "november":
    lastName = "Bengal"
  elif monthInput == "december":
    lastName = "Car"
  return lastName
    
print("What is your cat name?")
dayInput = int(input("Enter the day you were born (1 to 31) "))
monthInput = input("Enter the month you were born ").lower().strip()

firstName = findFirstName(dayInput)
lastName = findLastName(monthInput)
print("Your cat name is", firstName, lastName + "!")
