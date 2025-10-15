holiday = ['MLK Jr. Day', 'Presidents\' Day', 'Mother\'s Day', 'Memorial Day', 'Father\'s Day', 'Labor Day', 'Thanksgiving']
date = ['third Monday in January', 'third Monday in February', 'second Sunday in May', 'last Monday in May', 'third Sunday in June', 'first Monday in September', 'fourth Thursday in November']

idk = input('What holiday\'s date would you like to know? ').lower()
for x in range(len(holiday)):
    if idk == holiday[x].lower():
        print(holiday[x], 'is the', date[x])
    
