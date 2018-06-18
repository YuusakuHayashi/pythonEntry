class A:
    def sayHello(self):
        print("hello from class A")

class B:
    def sayHello(self):
        print("hello from class B")

class C(A, B):
    pass

c = C()
c.sayHello()

