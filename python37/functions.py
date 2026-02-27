def sum(val1,val2):
    return int(val1)+int(val2)
def sub(val1,val2):
    return int(val1)-int(val2)
def mul(val1,val2):
    return int(val1)*int(val2)
def div(val1,val2):
    return int(val1)/int(val2)

user=input("enter your value:-")

choose_operators=""
val1=0
val2=0

operators=["+","-","*","/"]

for i in range(len(user)):
    if (user[i] in operators):
        choose_operators=user[i]
        op=user.index(user[i])
        val1=user[0:op]
        val2=user[op+1:len(user)]



if choose_operators == "+":
    print("addition:-",sum(val1,val2))
elif choose_operators == "-":
    print("subtract:-",sub(val1,val2))
elif choose_operators == "*":
    print("multiply:-",mul(val1,val2))
elif choose_operators == "/":
    print("division:-",div(val1,val2))
else:
    print("Invalid Choice")

