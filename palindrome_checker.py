# Program to check whether inputed string is palindrome or not
string_input = input("Enter the String :- ")
if string_input == string_input[::-1]:
    print(f"Inputed string :- {string_input}, is palindrome")
else:
    print(f"Inputed String :- {string_input}, is not palindrome")