############DEBUGGING#####################

# # Describe Problem
# the problem is that the range (0,20) does not include the value of 20 therefore it wont print the statement
# changing 20 to 21 the range is from 1 - 20 rather than 1 - 19
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# randint(1,6) is incorrect as in an array the index first number is 0 so the correct answer is (0,5)
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# elif year > 1994 excludes if the user inputs 1994 in order to include 1994 as the Gen Z the correct statement
# would be elif year >= 1994
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# input is a string and then being used as a int when it hasnt been casted to an int
# in order to fix this use int(input("How old are you?"))
# also the {age} wont show the age *
# age = int(input("How old are you? "))
# if age > 18:
#   print(f"You can drive at age {age}.")

# #Print is Your Friend
# there is an error when putting word_per_page it should not have a double == sign which means a comparison rather
# than assignment
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words)

# #Use a Debugger
# indentation missing to line 55 which would only cause for the last item in the list to be appended to the new
#list
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])