#Program to make mulltiplication table from 1 to 10
my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print(f"Table of {i} ")
    for j in my_list:
        print(f"{i} * {j} = {i*j}")