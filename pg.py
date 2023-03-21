def change(num1, num2=50):
    num1 = num1+num2
    num2 = num1-num2
    print(num1,"#",num2)
    return(num1)
n1=150
n2=100
n1 = change(n1,n2)
"""yaha pr n1 = change(150,100) hai  :  then num1 = 150+100 = 250 hoga : aur num2 = 250-100 = 150 hoga 
phir 250#150 print hoga aur yeh return krdega n1 = 250"""
print(n1,"#",n2)
# ab yaha pr n1= 250 hai aur n2=100 so , 250#100 print hoga
n2 = change(n2)
"""yaha pr n1 = change(100,50)kyuki dekh yaha pr sirf ek value di hai to num1=100 hui 
aur dusri jo default de rkhi hai wo hui means num2=50 hai  :
then num1 = 100+50 = 150 hoga : aur num2 = 150-50 = 100 hoga 
phir 150#100 print hoga aur yeh return krdega n2 = 150"""
print(n1,"#",n2)
# ab humare pass n1=250 aur n2=150 hai to 250#150 print hoga