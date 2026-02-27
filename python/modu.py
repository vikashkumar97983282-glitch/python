def eq():
    a=float(input("enter no1:-"))
    b=float(input("enter no2:-"))
    print("1.add, 2.sub, 3.mul, 4.div")
    x=int(input("choose eq:-"))
    y=x.len()

    if (x==1):
        print("addition:-",a+b)
    elif (x==2):
        print("sub:-",a-b)
    elif (x==3):
        print("mul:-",a*b)
    elif (x==4):
        print("div:-",a/b)
    else:
        print("invalid choice! please valid choose eq")
eq()
