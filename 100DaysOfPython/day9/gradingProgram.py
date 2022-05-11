student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for scores in student_scores:
    if student_scores[scores] > 90 and student_scores[scores] <= 100:
        student_scores[scores] ="Outstanding"
        student_grades[scores] = student_scores[scores]
    elif student_scores[scores] > 80 and student_scores[scores] <= 90:
        student_scores[scores] ="Exceeds Expectations"
        student_grades[scores] = student_scores[scores]
    elif student_scores[scores] > 70 and student_scores[scores] <= 80:
        student_scores[scores] ="Acceptable"
        student_grades[scores] = student_scores[scores]
    else :
        student_scores[scores] ="Fail"
        student_grades[scores] = student_scores[scores]

# 🚨 Don't change the code below 👇
print(student_grades)