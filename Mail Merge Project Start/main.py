with open("Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    namer = names_file.readlines()

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letterc = letter_file.read()

    for line in namer:
        linestriped = line.strip()
        new_letter = letterc.replace("[name]", linestriped)
        with open(f"Mail Merge Project Start/Output/{linestriped}.txt", mode="w") as file:
            file.write(new_letter)