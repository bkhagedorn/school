food = [['Chic Fil A', 'Zaxby\'s', 'Popeye\'s', 'Famous Recipe'], ['McDonald\'s', 'DQ', 'Burger King', 'Five Guys'], ['Quizno\'s', 'Subway', 'Jersey Mike\'s', 'Potbelly']]

print('#1')
print(food[1])
print()

print('#2')
for i in range(len(food)):
    for x in range(len(food[i])):
        print(food[i][x], end=' ')
    print()
        
print()
food[0][3] = 'KFC'
food[2][3] = 'Penn Station'

print('#3')
for i in range(len(food)):
    print(food[i][3])
