#word = "zoo"
#
#fp = open("../ejdic-hand-utf8.txt", "r", encoding="utf-8")
#
#for line in fp:
#    if line.startswith(word):
#        print(line)
#fp.close()

import re

fdic = open("../ejdic-hand-utf8.txt", "rt", encoding="utf-8")

fw = open("q-list.txt", "wt")

for line in fdic:
    if re.match(r"q[a-z]{3}\s", line):
        fw.write(line)
        print(line.strip())

fw.close()
fdic.close()
