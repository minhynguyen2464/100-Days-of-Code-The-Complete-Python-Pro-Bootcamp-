#menu
print("Welcome to Python Pizza Deliveries!")
print("Small Pizza: $15")
print("Meidum Pizza: $20")
print("Large Pizza: $25")
print("Pepperoni for Small Pizza: +2$")
print("Pepperoni for Large Pizza: +3$")
print("Extra cheese for any size pizza: +1$")

#input
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#process
total_bill=0

if(size=="S"):
    total_bill+=15
elif(size=="M"):
    total_bill+=20
else:
    total_bill+=25
    
if add_pepperoni=='Y' and (size=='S' or size=='M'):
    total_bill+=2
else:
    total_bill+=3

if(extra_cheese=='Y'):
    total_bill+=1
    
#output
print(f"Your total bill is: {total_bill}$")