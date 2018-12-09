import re

txt = open("ejdic-hand-utf8.txt", "rt", encoding="utf-8").read()
lines = txt.split("\n")
print(len(lines))
words = list(map(lambda s: s.split("\t")[0], lines))

m = lambda pat: list(filter(lambda w: 1 if re.search(pat, w) else 0, words))

print(m(r"low$"))
