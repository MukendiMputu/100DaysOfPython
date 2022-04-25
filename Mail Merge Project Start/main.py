# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
guest_list = []

with open("Input/Names/invited_names.txt") as names:
    # Loop through the file line by line
    for name in names:
        guest_list.append(name.strip())

with open("Input/Letters/starting_letter.txt", "rt") as template:
    original_text = template.read()

for guest in guest_list:
    invite_text = original_text.replace("[name]", guest)
    with open(f"Output/ReadyToSend/letter_for_{guest}.txt", "wt") as letter:
        letter.write(invite_text)
