# iterater

scores = [40, 50, 60, 70, 80]
it = iter(scores)
print(next(it))
print(next(it))
print("hello")
print(next(it))

def GetInfinite():
    i = 0
    while True:
        yield i * 2
        i += 1

g = GetInfinite()
print(next(g))
print(next(g))
print(next(g))
