choose1=("addition")
choose2=("substraction")
choose3=("multiplication")
choose4=("division")
print(choose1)
print(choose2)
print(choose3)
print(choose4)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
a=int(input("enter the value:"))
b=int(input("enter the value:"))
choose=int(input("choose"))


if(choose==1):
    print(a,"+",b,"=",a+b)
elif(choose==2):
    print(a,"-",b,"=",a-b)
elif(choose==3):
    print(a,"*",b,"=",a*b)
elif(choose==4):
    print(a,"/",b,"=",a/b)
else:
    print("invalid")
