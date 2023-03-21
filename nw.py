fileobj = open('forest.txt', 'r')
R1 = (fileobj.readline().split())
for word in R1:
    for ch in range(len(word)-1,-1,-1):
        print(word[ch],end="")
print(end="")
fileobj.close()