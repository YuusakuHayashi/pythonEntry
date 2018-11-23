import sys

if len(sys.argv) <= 1:
    print("以下のように入力してください")
    print("python lesson11.py (住所)")
    sys.exit()

addr = sys.argv[1].strip()

fp = open("KEN_ALL.CSV", "rt", encoding="shift_jis")

for line in fp:
    line = line.replace(' ', '')
    line = line.replace('"', '')
    cells = line.split(",")
    zipno = cells[2]            # address
    ken = cells[6]              # prefecture
    shi = cells[7]              # city
    cho = cells[8]              # town, villege and so on...
    title = ken + shi + cho
    if title.find(addr) >= 0:
        print(zipno + ":" + title)
fp.close()
