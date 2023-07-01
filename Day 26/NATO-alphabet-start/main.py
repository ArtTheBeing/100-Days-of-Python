student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

##################################################################################################################################################

#TODO 1. Create a dictionary in this format:
words_df = pandas.DataFrame(pandas.read_csv("Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv"))
dictionary = {row.letter:row.code for (index,row) in words_df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Give me your name: ")
    #List of letters
    #Change all letters to upper
    name = [letter.upper() for letter in word]
    #Dont overthink... Just call the dictonary key for value
    try:
        name_dict = [dictionary[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(name_dict)
generate_phonetic()

    



