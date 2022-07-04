# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = weight / (height ** 2)
BMI = int(round(BMI, 0))

if BMI > 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")
elif 30 < BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif 25 < BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 18.5 < BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
else:
    print(f"Your BMI is {BMI}, you are underweight.")
