import random


# test_seed = random.random()*1
# whole_random = round(test_seed)

whole_random = random.randint(0, 1)

if whole_random == 1:
    print("Heads")
elif whole_random == 0:
    print("Tails")
