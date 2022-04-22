from tkinter import scrolledtext


print(8/3)
print(int(8/3))  # cuts off decimals
print(round(8/3))  # rounds
print(round(8/3, 2))
print(type(8/3))

score = 0
# user scores a point
score += 1
score -= 1
score /= 1
score *= 1
score = 98
print("Your Score = " + str(score))

# or
height = 1.8
isWinning = True
print(
    f"Your Score = {score}, your height is {height}, and you are winning is {isWinning}")
