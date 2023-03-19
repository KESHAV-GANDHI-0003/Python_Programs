# Program to add no till the user typeed "done"
user_input = input("Enter any random no. or done :- ")
sum = 0
while user_input != "done":
    sum = sum + int(user_input)
    user_input = input("Enter any random no. or done :- ")
print(f"Sum of no. you entered :- {sum}")
