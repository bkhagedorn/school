class Candy():
    def __init__(self, a, b, c):
        self.name = a
        self.flavor = b
        self.calories = 100
        self.ok_braces = True
        self.price = c

    def taste(self):
        print(self.name + " candy is " + self.flavor + ".")

    def sale_price(self):
        return self.price / 2

    def ortho(self):
        if not self.ok_braces:
            print("You shouldn't eat " + self.name + " candy if you have braces.")
        else:
            print(self.name + " candy is orthodontist approved!")

    def cost_per_calorie(self):
        if self.calories == 0:
            return 0
        else:
            x = self.price / self.calories
            return "%.3f" % x

pd = Candy("PayDay", "peanutty", 1.06)
eg = Candy("Extra Gum", "minty", 1.59)
fd = Candy("Fun Dip", "fruity", 1.29)
fd.calories = 50
fd.ok_braces = False
sfc = Candy("Starburst Fruit Chews", "fruity", 0.89)
sfc.calories = 160
sfc.ok_braces = False
st = Candy("Sweet Tarts", "sour", 0.99)
st.calories = 60
ah = Candy("Air Heads", "fruity", 0.49)
ah.calories = 120
ah.ok_braces = False
boh = Candy("Bit O'Honey", "honey-flavored", 0.98)
boh.calories = 150
boh.ok_braces = False

prices = [pd.sale_price(), eg.sale_price(), fd.sale_price(), sfc.sale_price(), st.sale_price(), ah.sale_price(), boh.sale_price()]

pd.calories = 240
pd.taste()
print(pd.name, "candy is on sale today for", str(pd.sale_price()) + ".")
pd.ortho()
print(pd.name, "candy cost", "$" + str(pd.cost_per_calorie()), "per calorie.")

print()
print("---")
print()

print("#1")
print(sfc.name + ", " + str(sfc.calories) + " calories.")
print("#2")
print("$" + str(st.cost_per_calorie()))
print("#3")
eg.ortho()
print("#4")
print("$" + str(fd.cost_per_calorie()))
print("#5")
ah.taste()

counter = 0
for i in prices:
    if i < 0.50:
        counter += 1
print("There are", counter, "candies in the store the cost less than 50 cents.")
