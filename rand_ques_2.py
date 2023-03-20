x = "apple,peach,pear,grapefruit"
y = x.split(",")
print(y)
for z in y:
    if z <'m':
        print(str.lower(z))
    else:
        print(str.upper(z))