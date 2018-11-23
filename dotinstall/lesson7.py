score = int(input("score? "))

if score > 80:
    print("Great")
elif score > 60:
    print("Good")
else:
    print("so so..")

msg = "you passed the exam" if score > 55 else "you failed the exam you must retest"

print(msg)
