class Human:
    population = 0
    domain = "H. sapiens"

    def __init__(self, n, x, p):
        Human.population += 1
        self.name = n 
        self._sex = x
        self._personalities = p
        print("-- %s was born" % self.name)

    def eat(self, food):
        print("-- %s eat %s" % (self.name, food))

    @classmethod
    def showPopulation(cls):
        print("-- amount of population: %d" % cls.population)

class SuperHuman(Human):
    def __init__(self, n, x, p):
        super().__init__(n, x, p)
