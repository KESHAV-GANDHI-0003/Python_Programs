#Prgram to check first no is divisible by 2 or not
input_1 = int(input("Enter no. 1 :-"))
input_2 = int(input("Enter no. 2 :-"))
if input_1 % input_2 == 0:
    print(f"{input_1} is divisible by {input_2}")
else:
    print(f"{input_1} is not divisible by {input_2}")