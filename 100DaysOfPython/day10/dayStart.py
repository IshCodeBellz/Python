def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        """ Take a first and last name and format it to return the title case version of the name"""
        return print("You didnt provide any valid inputs.")
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return print(f"Result: {formatted_f_name} {formatted_l_name}")


format_name(f_name=input("What is your name? "), l_name=input("What is your last name? "))
