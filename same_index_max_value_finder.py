# Program to find max tuple value at same index in dictionary
my_points={'a': (4, 3), 'b': (1, 2), 'c': (5, 1)}
highest = [0, 0]
init = 0
for a in range(2):
    init = 0
    for b in my_points.keys():
        # print(b)
        # print(a)
        val = my_points[b][a]
        # print(val)
    if init == 0:
        highest[a] = val
        # print(val)
    init += 1
    if val > highest[a] :
        highest[a] = val
        # print(val)
    print("Maximum Value at index(my points, ", a, ") = ", highest[a])