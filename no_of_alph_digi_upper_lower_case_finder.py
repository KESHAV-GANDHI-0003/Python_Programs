# Program that reads a lines and find the no of digits, alphabets , lowercase and uppercase
no_of_digits = 0
no_of_alphabets = 0
no_of_uppercase = 0
no_of_lowercase = 0
line = input("Enter a line :- ")
for i in line:
    if (i.isalpha()) == True :
        no_of_alphabets += 1
        if (i.isupper()) == True:
            no_of_uppercase +=1
        else:
            no_of_lowercase += 1
    elif (i.isdigit()) == True:
        no_of_digits += 1
print(f" No. of Digits :- {no_of_digits}\n No. of Alphabets = {no_of_alphabets} \n No. of Uppercase = {no_of_uppercase} \n No. of Lowercase = {no_of_lowercase} ")