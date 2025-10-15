'''
Brayden Hagedorn
11/29/2023
Class List
'''
classes = [[1, 'Scott', 'Computer Science'], [2, 'Mumaw', 'Physics'], [3, 'McGarvey', 'English'], [4, 'Philpot', 'Spanish'], [5, 'Cooley', 'Weighlifting'], [6, 'Thomas', 'Orchestra'], [7, 'Dillon', 'Math']]
print(classes[3])
print(classes[0][1])
print(classes[5][2])
print(classes[6][0])

for i in range(len(classes)):
    print()
    print(classes[i])
print()

for i in range(len(classes)):
    print()
    for x in range(3):
        print(classes[i][x], end=' ')
