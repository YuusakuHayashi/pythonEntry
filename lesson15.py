class User:
    description = "User instace is made about login-user"
    def __init__(self, name):
        self.name = name 


print(User.description)
bob = User("bob")
print(bob.description)
