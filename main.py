# love calculator using scientific method explained as per
# https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love

print("Welcome to the Love Calculator!")
name1 = input("What is your name? : ").lower()
name2 = input("What is their name? : ").lower()
namesCombined = name1 + name2
trueCount = 0
loveCount = 0
t = namesCombined.count("t")
r = namesCombined.count("r")
u = namesCombined.count("u")
e = namesCombined.count("e")
trueCount += t + r + u + e

l = namesCombined.count("l")
o = namesCombined.count("o")
v = namesCombined.count("v")
e = namesCombined.count("e")
loveCount += l + o + v + e
count = int(str(trueCount) + str(loveCount))

if count > 100:
    count -= 100

if count < 10 or count > 90:
    print(f"Your compatibility is {count}%, you two go together like coke and mentos!")
elif 40 <= count <= 50:
    print(f"Your compatibility is {count}%, you are alright together.")
else:
    print(f"Your compatibility is {count}%")

