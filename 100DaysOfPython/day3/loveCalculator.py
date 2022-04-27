# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
nameTogether = name1.lower()+name2.lower()
t = nameTogether.count("t") + nameTogether.count("r") + \
    nameTogether.count("u") + nameTogether.count("e")

l = nameTogether.count("l") + nameTogether.count("o") + \
    nameTogether.count("v") + nameTogether.count("e")

trueLove = (t * 10) + l

if trueLove < 10 or trueLove > 90:
    print(f"Your score is {trueLove}, you go together like coke and mentos.")
elif trueLove >= 40 and trueLove <= 50:
    print(f"Your score is {trueLove}, you are alright together.")
else:
    print(f"Your score is {trueLove}")

# print(trueLove)
