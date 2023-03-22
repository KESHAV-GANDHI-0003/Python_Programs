l=[]
l1=['hi', 'to', 'all']
S=""
for j in l1:
    S=""
    x=j
    for i in x.lower():
        S=""
        if i in ("aeiou"):
            continue
        else:
            S+=i
            l=l+[S]
l_1=[]
kk=""
for i in l:
    kk+=i
l_1.append(kk)
print(l_1)