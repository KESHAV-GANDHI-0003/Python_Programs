#Program to sort list using bubble sort
list_1 = eval(input("Enter the list using square brackets :- "))
list_length = len(list_1)
for i in range(list_length):
    for j in range(list_length-i-1):
        if list_1[j] > list_1[j+1]:
            list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
print(f"Sorted List :- {list_1}")