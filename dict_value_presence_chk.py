# Program to check if the value is present or not
dict_1 = {"Keshav":"Sci", "Govind":"Com", "Nimai":"Humanities"}
value_1 = input("Enter the value which you want to check :- ")
dict_values = dict_1.values()
for keys,values in dict_1.items():
    if value_1 == values.lower():
        print(f"{value_1} is present in Dictionary \n Key of {value_1} is {keys}")