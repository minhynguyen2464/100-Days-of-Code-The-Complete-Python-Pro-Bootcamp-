#input
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name \n").lower()

#process
name = name1+" "+name2
#truelov
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")

true = t+r+u+e
love = l+o+v+e
result = str(true) + str(love)
love_score = int(result)

#outputs
if(love_score<10) or (love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(love_score<50) and (love_score>40):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")