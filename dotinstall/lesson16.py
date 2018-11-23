class User:
    description = "User instace is made about login-user"
    def __init__(self, name):
        self.name = name 
    def sayHello(self):
        print("hi %s" % self.name)

    @classmethod
    def show_info(cls):
        print("info: %s" % cls.description)

User.show_info()
bob = User("bob")
bob.sayHello()
