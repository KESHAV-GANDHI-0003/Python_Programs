value=60
def display(n):
    global value
    value = 25
    if n%7==0:
        value=value+n
    else:
        value=value-n
print(value,end="#")
display(10)
print(value)