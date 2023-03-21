# Program to sort list using insertion list
list_1 = eval(input("Enter the List using square brackets :- "))
list_length = len(list_1)
for i in range(list_length):
    k = list_1[i]
    j = i-1
    while j>=0 and k <list_1[j]:
        list_1[j+1] = list_1[j]
        j=j-1
    else:
        list_1[j+1] = k
print(f"Sorted List :- {list_1}")