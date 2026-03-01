while True:

    a=input("enter the value:-")
    x=[]
    y=[]
    d=[]


    operators=["+","-","*","/"]


    for i in range(len(a)):
    
        if a[i] in operators:
            d=a[i]          # store the opeartors in d
            v=a.index(d)       # store operators index in v
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
    










'''list=[]
for i in range(1):
    user=input("enter the element:-")
    #user=user.split()
    list.append(user)
print(list)
#a=list[0][0]
#b=list[0][2]
#print(int(a)+int(b))'''




















































'''questions=[]

for i in range(0,3):
    q=input(f"enter the questions{i+1} :-")
    questions.append([q])
    for j in range(1,5):
        q=input(f"enter the options{j}:-")
        questions[i].insert(j,q)  #adding element specific index
print(questions)'''
