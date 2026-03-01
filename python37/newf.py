a=input("enter the value:-")
x=[]
y=[]
d=[]


operators=["+","-","*","/"]


for i in range(len(a)):
    
    if a[i] in operators:
        d=a[i]          # store the opeartors in d
        v=a.index(d)       # store index in v
        x=a[0:v]         # store 0 index from before operators
        y=a[v+1:len(a)]    # store after operators from length of value
        
        
if d == "+":
    print(int(x)+int(y))
elif d == "-":
    print(int(x)-int(y))
elif d == "*":
    print(int(x)*int(y))
elif d == "/":
    print(int(x)/int(y))
elif d == "%":
    print(int(x)//int(y))
else:
    print(invalid)

