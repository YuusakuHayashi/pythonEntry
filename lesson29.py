# map, lambda

def triple(n):
    return n * 3

ml = list(map(triple, [1, 2, 3]))
print(ml)

l = list(map(lambda n: n*3, [1, 2, 3]))
print(l)
