# Program to convert feet to inches
def feet_to_inches_con (length):
    inch = length*12
    print(f" {length} is equal to {inch} inches")
feet_to_inches_con(10)

def feet_to_inch_con ():
    no_of_feet = int(input("Enter no of feet :- "))
    inch = no_of_feet*12
    print(f"{no_of_feet} is equal to {inch} inches")
feet_to_inch_con()
def inch_to_feet_con ():
    no_of_inch = int(input("Enter no of inches :- "))
    feet = no_of_inch / 12
    print(f"{no_of_inch} is equal to {feet} inches")
inch_to_feet_con()