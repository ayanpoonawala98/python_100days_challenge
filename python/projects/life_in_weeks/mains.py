# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rem_days = 90 - int(age)
days = (int(rem_days)*365)
month = (int(rem_days)*12)
weeks = (int(rem_days)*int(365/7))
# print("You have " + str(days) + " days, "+ str(weeks) + " weeks, " + "and " + str( month) + " months left.")

print(f"You have {days} days, {weeks} weeks, and {month} months left.")


