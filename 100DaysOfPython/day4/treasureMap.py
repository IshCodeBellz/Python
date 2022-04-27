# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# or
# position1/horizontal = position[0] for first number
# position2/vertical = position[1] for second number
position = int(position)

position1 = int(position / 10) - 1
position2 = int(position % 10) - 1
map[position1][position2] = "X"
# print(position1)
# print(position2)


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
