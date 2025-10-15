golfScores = [78, 81, 75, 86, 74]
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
recipes = ['vegetable lasagna', 'red curry', 'jambalaya', 'chicken enchiladas', 'falafel']
teachers = ['Kristen Scott', 'Clark Mumaw', 'Nathan McGarvey', 'Jessica Philpot', 'Steven Cooley', 'Angela Thomas', 'Jacqueline Dillon']
desserts = ['frozen yogurt', 'bread pudding', 'hummingbrid cake', 'baklava', 'apple pie', 'churros']
testScores = [99, 86, 65, 100, 91, 76]

print(golfScores)
print(colors)
print(recipes)
print(teachers)
print(desserts)
print(testScores)

print('#1')
print(golfScores[0])
print()

colors[5] = 'Indigo'
colors.append('Violet')

print('#3')
for i in colors:
    print(i)
print()

recipes[0] = 'Spaghetti'
desserts[0] = 'mint choc. chip ice cream'

print('#6')
for i in teachers:
    print(i)
print()

print('#7')
for i in range(len(desserts)):
    print(desserts[i])
print()

print('#8')
for i in recipes:
    print(i, '', end='')

total = 0
for i in testScores: 
    total += i

print()
print()
print('#10')
average = total / len(testScores)
print(average)
