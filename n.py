x = 3
def myfunc():
    global x
    x+=2
    print(x, end='')
print (x, end="")
myfunc()
print(x, end=' ')