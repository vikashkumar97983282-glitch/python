def cal(a,b):
    c= int(input("enter your choise"))
    d=0
    if (c==1):
        d=a+b
        return print(d)
    elif(c==2):
        d=a-b
        return d
    elif(c==3):
        d=a*b
        return d
    elif(c==4):
        d=a/b
        return d

a=int(input("enter your number"))
b=int(input("enter your number"))
cal(a,b)
