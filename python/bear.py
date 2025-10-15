class Bear:
    def __init__(self, n, f, t, b):
        self.name = n
        self.face = f
        self.torso = t
        self.bottom = b

    def mood(self):
        print(self.name, "is in a", self.face, "mood.")

    def outfit(self):
        print(self.name, "is wearing", self.torso, "and", self.bottom + ".")

ted = Bear("Teddy", "very happy", "a pajama top", "jeans")
ted.outfit()

cranky = Bear("Cranky", "mad", "a tanktop", "underwear")
cranky.mood()
cranky.outfit()

big = Bear("Big", "sleepy", "an oversized t-shirt", "shorts")
big.mood()
big.outfit()
