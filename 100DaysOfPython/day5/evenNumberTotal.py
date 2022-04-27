# Write your code below this row 👇
total = 0
for numbers in range(0, 101, 2):
    total += numbers
print(total)


total2 = 0
for numbers in range(0, 101):
    if numbers % 2 == 0:
        total2 += numbers

print(total2)
