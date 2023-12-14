import random

names_string = input("Give me everybody's names, seperated by a comma: ")
names = names_string.split(",")

bill_person = random.choice(names)

print(f"Person who pay the bill is {bill_person}")