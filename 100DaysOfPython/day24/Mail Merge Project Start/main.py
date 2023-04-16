# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
new_name_list = []

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()
    for name in names:
        new_name_list.append(name.strip("\n"))
    # print(new_name_list)

for name in new_name_list:
    with open(f"../Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as name_letter:
        read = name_letter.read()
        new_script = read.replace("[name]", name)

        with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as complete_letter:
            complete_letter.write(new_script)
