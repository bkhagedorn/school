class Youtuber:
    def __init__(self, n, s, g, y):
        self.name = n
        self.subscribers = s
        self.genre = g
        self.year = y

    def info(self):
        return self.name + " has been making videos about " + self.genre + " since " + str(self.year) + " and currently has " + str(self.subscribers) + " subscribers."

    def add_subs(self, subs):
        self.subscribers += subs

    def influencer(self):
        if self.subscribers > 10000:
            return self.name + " is an influencer"
        else:
            return self.name + " is not an influencer"
    
mark = Youtuber("Markiplier", 365000000, "Gaming, Variety", 2012)
beast = Youtuber("Mr. Beast", 244000000, "Challenges", 2012)
jack = Youtuber("jacksepticeye", 30600000, "Entertainment, Reaction, Vlogs, Gaming", 2007)
sauce = Youtuber("Vsauce", 21300000, "Educational", 2007)

print(mark.info())
print(beast.info())
print(jack.info())
print(sauce.info())

mark.add_subs(500000)
beast.add_subs(500000)
jack.add_subs(500000)
sauce.add_subs(500000)

print()
print(mark.info())
print(beast.info())
print(jack.info())
print(sauce.info())

print()
print(mark.influencer())
print(beast.influencer())
print(jack.influencer())
print(sauce.influencer())
