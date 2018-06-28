# list type

scores = [40, 50]
print(scores[0])
scores[0] = 95 
print(scores[0])
print(len(scores))
scores.append(100)
print(scores)

for i, score in enumerate(scores):
    print("{0}: {1}".format(i, score))
