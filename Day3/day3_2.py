weight = float(input("Enter you weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = round(weight/height**2,1)

print(f"Your BMI is: {bmi}")

if(bmi<18.5):
    print("You are underweight")
elif(bmi<25):
    print("You are normal weight")
elif(bmi<30):
    print("You are overweight")
elif(bmi<35):
    print("You are obese")
else:
    print("You are clinically obese")