room_list = []

###
# Room creation
# 0/Cryogenic Chamber
room = ['You are in the Cryogenic Chamber. There is a passage to the North.', 1, None, None, None]
room_list.append(room)
# 1/Hall
room = ['You are in the Hall. There are passages in every direction.', None, None, 0, 2]
room_list.append(room)
# 2/Entertainment Room
room = ['You are in the Entertainment Room. There are passages to the East, South, and West', None, 1, 4, 3]
room_list.append(room)
# 3/Bathroom
room = ['You are in the Bathroom. There is a passage to the East.', None, 2, None, None]
room_list.append(room)
# 4/Kitchen
room = ['You are in the Kitchen. There is a passage to the North.', 2, None, None, None]
room_list.append(room)
# 5/Control Room
room = ['You are in the Control Room. There is a passage to the South and West.', None, None, 6, 1]
room_list.append(room)
# 6/Maintanence Closet
room = ['You are in the Maintanence Closet. There is a passage to the North.', 5, None, None, None]
room_list.append(room)
###

current_room = 0
done = False
choice = ''
direction = ''
next_room = 0
firstTime = True

# required stuff
keycard = False
key1Collected = False
key2Collected = False
finalDoorOpen = False

# intro
print('(Press enter to continue with dialogue)')
d = input('You feel a droning in your head while you slowly open your eyes.')
d = input('You slowly climb out of a metal device and into a large open room.')

while not done:
  print('- - -')
    
  print(room_list[current_room][0])

  # Choices
  print('What would you like to do?')
  print()
  if firstTime:
    print('(Enter a number.)')
    firstTime = False
  print('1) Inspect Room') # i NEED to add personality to this
  print('2) Leave')
  print()
  choice = input('')

  # Choice 1/Inspect Room
  if choice == '1':
    if current_room == 0:
      d = input('This room is REALLY dusty.')
      d = input('...You don\'t think anyone has been here for a while.')
      d = input('There is another metal device across the room from the one you came out of.')
      d = input('You go over to inspect it.')
      d = input('...there isn\'t anyone in there.')
    elif current_room == 1:
      d = input('This is a long hallway.')
      d = input('...long, only for there to be LITERALLY NOTHING in it.')
      d = input('...')
      d = input('Hold on, is that a mirror?')
      d = input('You go over to the very end of the hallway and look at yourself in the mirror.')
      d = input('...')
      d = input('It\'s you.')
    elif current_room == 2:
      if not keycard:
        d = input('Wow.')
        d = input('This is a REALLY sad "enterainment" room.')
        d = input('There is literally only a single TV in here.')
        d = input('Not even any chairs or anything.')
        d = input('...do you wan\'t to turn on the TV? (Y/N) ').lower().strip()
        if d == 'y':
          d = input('Are you sure? It might be haunted...')
          d = input('...something might crawl out of it.')
          d = input('Eh, whatever.')
          d = input('You go over and press the power button.')
          d = input('...it doesn\'t turn on.')
          d = input('Probably should\'ve expected this place to have no power.')
          d = input('...')
          d = input('...is there something under the TV?')
          d = input('You check under the TV.')
          d = input('...there\'s a keycard.')
          d = input('You took the keycard.')
          keycard = True
          room_list[1][2] = 5
        elif d == 'n':
          d = input('Fair enough.')
      else:
        d = input('Wow.')
        d = input('This is a REALLY sad "enterainment" room.')
        d = input('There is literally only a single TV in here.')
        d = input('Not even any chairs or anything.')
        d = input('...')
    elif current_room == 3:
      if not key1Collected:
        d = input('Yep.')
        d = input('This is certainly a bathroom.')
        d = input('...')
        d = input('...do you need to go or something? (Y/N) ').lower().strip()
        if d == 'y':
          d = input('Well, go ahead then.')
          d = input('You open the stall door.')
          d = input('...')
          d = input('...ok.')
          d = input('There is no toilet.')
          d = input('A key lays on the ground in the place it should be.')
          d = input('You pick up the key.')
          key1Collected = True
      else:
        d = input('Yep.')
        d = input('This is certainly a bathroom.')
    elif current_room == 4:
      d = input('I don\'t think a kitchen usually has this much dust.')
      d = input('There\'s a fridge in the corner.')
      d = input('...do you want to open it? (Y/N) ')
      d = input("Actually, nevermind, you will DEFINITELY die if you eat any food in there.")
    elif current_room == 5:
      if not finalDoorOpen:
        d = input('There are two key slots and a locked button that says "OPEN EXIT."')
        if not key1Collected and not key2Collected:
          d = input('...')
          d = input('At least they didn\'t make it vague.')
        elif (key1Collected and not key2Collected) or (key2Collected and not key1Collected):
          d = input('You already found one key, now you just need to find the last one.')
        elif key1Collected and key2Collected:
          d = input('You insert both of the keys and twist them.')
          d = input('The barrier protecting the button lifts up and it lights up.')
          d = input('You press the button.')
          d = input('...')
          d = input('You can leave now.')
          finalDoorOpen = True
      else:
        d = input('You can leave now.')
    elif current_room == 6:
      if not key2Collected:
        d = input('This is a really small closet.')
        d = input('You try to leave, but you accidentally knock into the shelf.')
        d = input('A bucket falls onto the floor, and a key slips out of it.')
        d = input('You pick up the key.')
        key2Collected = True
      else:
        d = input('You feel claustrophobic.')
    
  # Choice 2/Leave
  if choice == '2': # why doesn't this work with integers
    direction = input('Where do you want to go? ').strip().lower()
    if direction == 'north':
      next_room = room_list[current_room][1]
    elif direction == 'east':
      next_room = room_list[current_room][2]
    elif direction == 'south':
      next_room = room_list[current_room][3]
    elif direction == 'west':
      next_room = room_list[current_room][4]
    else:
      print('Enter a proper direction.')

    # Handling room stuff
    if next_room == None:
      if current_room == 1 and not finalDoorOpen and direction == 'north':
        d = input('There\'s a door.')
        d = input('You try and open it. It doesn\'t budge.')
        d = input('You bang on it.')
        d = input('...nothing.')
      elif current_room == 1 and not keycard and direction == 'east':
        d = input('There\'s a door.')
        d = input('There seems to be a keycard reader next to it.')
        d = input('...you have a feeling you won\'t be able to open it.')
      elif current_room == 1 and finalDoorOpen and direction == 'north':
        print()
        d = input('It\'s done.')
        d = input('You escaped.')
        d = input('You see a light at the end of the tunnel you\'re in.')
        d = input('You walk towards it.')
        print()
        print('GAME OVER')
        done = True
      else:
        print('You can\'t go that way.')
    else:
      current_room = next_room
