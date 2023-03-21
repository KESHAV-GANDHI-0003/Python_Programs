# Program that takes string and capatilize each word and generates a new string
string_input = input("Enter the String :- ")
string_list = string_input.split(" ")
new_string = ""
for i in string_list:
    if i[0].isupper():
        new_string += i
    elif i[0].islower():
        first_char = i[0].upper()
        i = i[1:]
        char_ = first_char+i+" "
        new_string += char_
print(f"Original String :- {string_input}\nNew String :- {new_string}")