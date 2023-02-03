student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass
import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data)

nato_alphabet = {row.letter:row.code for index, row in data.iterrows()}
print(nato_alphabet)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_text = input("input your name: ").upper()

alphabet_list  =[]
for letter in input_text:
    # print(type(letter))
    for k, v in nato_alphabet.items():
        if letter == k:
            alphabet_list.append(v)

print(alphabet_list)

# TODO 3. make list comprehension
output_list = [nato_alphabet[letter] for letter in input_text]
print(output_list)
