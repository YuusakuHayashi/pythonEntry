import myPackage.HumanModule as myHuman

myHuman.Human.showPopulation()
person = myHuman.Human("tom", "male", "gentle")
print("-- domain is %s" % person.domain)
myHuman.Human.showPopulation()
person.eat("sushi")

sperson = myHuman.SuperHuman("ken", "male", "arogant")
