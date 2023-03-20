# Program to find the index of tuple without using index() method
tuple_input = eval(input("Enter the tuple :- "))
no = int(input("Enter the number whoose index you want to find :- "))
index = -1
for i in tuple_input:
    index += 1
    if i == no :
        print(f"Index of {no} is {index}")