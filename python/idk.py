import random

states = ['North Carolina', 'Pennslyvania', 'North Dakota', 'Hawaii', 'Minnesota', 'Maryland', 'Alaska', 'New York', 'Colorado', 'Missouri']
gpas = []
schools = []
mascots = []
rannums = []

#1
x = 0
for i in states:
    print(states[x])
    x += 1
states.sort()
print()
print(states)
print()
print(states[0])
print()

#2
for i in range(5):
    gpa_input = int(input('Enter a GPA '))
    gpas.append(gpa_input)  
gpas.sort()
print()
print(gpas)
print()
print(gpas[-1])
print()

#3
for i in range(5):
    school_input = input('Enter a school ')
    schools.append(school_input)
    mascot_input = input('Enter that school\'s mascot ')
    mascots.append(mascot_input)
    print()
idkman = input('Which school\'s mascot would you like to know? ').lower()
for i in range(len(schools)):
    if idkman == schools[i].lower():
        print(schools[i] + '\'s mascot is the', mascots[i])

#5
z = 0
for i in range(10):
    z = random.randrange(1, 1000)
    rannums.append(z)
print(rannums)
print()
rannums.sort()
y = 0
for i in rannums:
    print(rannums[y])
    y += 1

