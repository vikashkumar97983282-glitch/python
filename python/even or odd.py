a=int(input("enter the value:"))

if(a>0):
    print(a,"is the positive")
    if(a%2==0):
        print(a,"is the even number")
    else:
        print(a,"is the odd number")
elif(a<0):
    print(a,"is the negative")
    if(a%2==0):
        print(a,"is the even number")
    else:
        print(a,"is the odd number")
else:
    print(a,"is the zero")
    print(a,"is the positive")
