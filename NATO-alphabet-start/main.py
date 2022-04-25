student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
en_nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
de_nato_dataframe = pandas.read_csv("deutsches_buchstabieralphabet_DIN5009.csv")
en_nato_dict = {row.letter: row.code for index, row in en_nato_dataframe.iterrows()}
de_nato_dict = {row.buchstabe: row.code for index, row in de_nato_dataframe.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word to spell ")
en_nato_spelling = [en_nato_dict[letter.upper()] for letter in user_input]
de_nato_spelling = [de_nato_dict[letter.upper()] for letter in user_input]


print("English NATO spelling: ", en_nato_spelling)
print("Deutsches DIN5009 Buchstabierung: ", de_nato_spelling)
