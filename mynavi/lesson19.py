import os, glob, time

l = [f for f in glob.glob("*") if os.stat(f).st_mtime > time.time() - 60*60*24]

print(l)

kuku = [(x, y, x*y) for x in range(1,10) for y in range(1,10)] 

s = ""

for x,y,z in kuku:
    s += "{0:5d}".format(z)
    if y == 9: s += "\n"
print(s)
