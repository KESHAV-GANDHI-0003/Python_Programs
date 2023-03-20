# Program to calculate time etween the time entered in military format
input_time_1 = int(input("Enter first time :-"))
input_time_2 = int(input("Enter second time :-"))
time = str(input_time_2-input_time_1)
print(time)
if len(time) == 3:
    no_of_hrs = time[0:1]
    no_of_mins = time[1:4]
elif len(time) == 2:
    no_of_hrs = 0
    no_of_mins = time[0:4]
else:
    no_of_hrs = time[0:2]
    no_of_mins = time[2:5]
print(f" Time between inputeed times :- {no_of_hrs} hrs {no_of_mins} mins ")