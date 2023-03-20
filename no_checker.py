#Progra, to check no is negative or zero or positive
user_input = int(input("Enter the no - "))
if user_input == 0:
    print("No. is zero")
elif user_input > 0:
    print("No. is postive")
elif user_input < 0:
    print("No. is negative")
else:
    print("Wrong Input")