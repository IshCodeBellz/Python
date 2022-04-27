import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

print(names)
length_names = len(names)
print(length_names)

# random_number = random.random() * length_names
random_number = random.randint(0, length_names-1)
print(random_number)
# rounded_random_number = round(random_number)
# random.choice(names) -- will select a random name from the list
paying_person = names[random_number]
print(f"{paying_person} is going to buy the meal today!")
#james, julia, janet, jennifer, jacob, john
