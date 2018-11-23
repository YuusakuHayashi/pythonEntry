sales = {"hayashi": 200, "yuusaku": 500}
print(sales["hayashi"])
sales["huruhata"] = 600
print(sales)
del(sales["yuusaku"])
print(sales)

for key, val in sales.items():
    print("%s: %d" % (key, val))
