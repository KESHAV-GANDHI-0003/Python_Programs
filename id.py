import random
POINTS= [20,40,10,30,15]
BEGIN= random.randint(1,3)
LAST=random.randint(2,4)
for C in range (BEGIN, LAST+1):
    print(POINTS[C],'#')