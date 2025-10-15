class Wizard:
    def __init__(self, n, h, p, w):
        self.name = n
        self.age = 11
        self.school = "Hogwarts"
        self.house = h
        self.patronus = p
        self.wand_core = "dragon heartstring"
        self.wand_length = w
        
    def get_patronus(self):
        return self.patronus

    def personal_info(self):
        print(self.name, "is", self.age, "years old and has a wand with a core of", self.wand_core + ".")

    def school_info(self):
        return self.name + " belongs to the House of " + self.house + " at " + self.school + "."
        
    def expelliarmus(self, obj):
        obj.wand_length = 0
        print(self.name, "has disarmed", obj.name)

    def birthday(self):
        self.age += 1
        
HarryP = Wizard("Harry Potter", "Gryffindor", "Stag", 11)
RonW = Wizard("Ron Weasley", "Gryffindor", "Jack Russell Terrier", 14)
HermoineG = Wizard("Hermione Grangier", "Gryffindor", "Otter", 15)
DracoM = Wizard("Draco Malfoy", "Slytherin", None, 15)
CedricD = Wizard("Cedric Diggory", "Hufflepuff", "Badger", 12.24)
NewtS = Wizard("Newt Scamander", "Hufflepuff", "Kelpie", 14)
FleurD = Wizard("Fleur Delacour", "Bellefeuille", "Non-corporeal", 9.5)

names = [HarryP, RonW, HermoineG, DracoM, CedricD, NewtS, FleurD]

print(HarryP.name, "has a patronus of a", HarryP.get_patronus() + ".")
print(RonW.name, "has a patronus of a", RonW.get_patronus() + ".")
print(HermoineG.name, "has a patronus of an", HermoineG.get_patronus() + ".")
print(DracoM.name, "has a patronus of a", str(DracoM.get_patronus()) + ".")

print()
print("---")
for i in names:
    print()
    i.personal_info()
    print(i.school_info())
print()
HermoineG.expelliarmus(DracoM)
DracoM.birthday()
print(DracoM.age)

for i in range(3):
    FleurD.birthday()
    CedricD.birthday()
NewtS.age = 97

DracoM.expelliarmus(FleurD)
print()
print("---")
for i in names:
    print()
    i.personal_info()
    print(i.school_info())
