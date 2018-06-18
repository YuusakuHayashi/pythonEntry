class Human:
    population = 0
    domain = "H. sapiens"

    def __init__(self, n, x, p):
        Human.population += 1
        self.name = n 
        self.sex = x
        self.personalities = p
        print("-- %s was born" % self.name)

    def eat(self, f):
        print("-- %s eat %s" % (self.name, f))

    @classmethod
    def showPopulation(cls):
        print("-- amount of population: %d" % cls.population)

Human.showPopulation()
person = Human("tom", "male", "gentle")
print("-- domain is %s" % person.domain)
Human.showPopulation()
person.eat("sushi")
