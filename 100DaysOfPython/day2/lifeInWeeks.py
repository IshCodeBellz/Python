# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

ageInt = int(age)
yearsLeft = 90 - ageInt

weeksLeft = yearsLeft * 52
monthsLeft = yearsLeft * 12
dayLeft = yearsLeft * 365

print(
    f"You have {dayLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")
