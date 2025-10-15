awesome = ['Splatoon', 'Half-Life', 'Terraria', 'Fortnite', 'Super Mario Wonder']

print('#1')
print(awesome)
print()

print('#2')
print(awesome[4])
print()

print('#3')
awesome.append('Castle Crashers')
print()

print('#4')
for i in awesome:
    print(i)
print()

print('#5')
for i in range(len(awesome)):
    print(awesome[i], '', end='')
print()
