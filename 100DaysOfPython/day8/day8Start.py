# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello")
  print("Hi")
  print("Bonjour")

greet()

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"Hi {name}")
#   print(f"Bonjour {name}")

# greet_with_name("john")

def greet_with_name(name,location):
  print(f"Hello {name}")
  print(f"My name is Yemi and im from {location}")
  print(f"Bonjour {name}")

greet_with_name(name = "john", location ="London")