#Program which takes input an print sum
int_input = int(input("Enter the no. :-"))
sum = 0
if int_input > 0:
    for i in range (int_input,(2*int_input)):
        sum += i
else:
    for i in range ((2*int_input),int_input,-1):
        sum += i
print(sum)