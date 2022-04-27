# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total_height = 0
number_of_scores = 0
for student in student_heights:
    total_height = total_height + student
    number_of_scores = number_of_scores + 1

average = round(total_height/number_of_scores)
print(average)
