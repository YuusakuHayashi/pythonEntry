msg = "hello"

def greetHello():
    global msg
    msg = "hello grobal from def"
    print(msg)

print(msg)
greetHello()
