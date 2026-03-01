while True:
    def sum(val1,val2):
        return int(val1)+int(val2)
    def sub(val1,val2):
        return int(val1)-int(val2)
    def mul(val1,val2):
        return int(val1)*int(val2)
    def div(val1,val2):
        return int(val1)/int(val2)

    user=input("Do Your Calculations:-")

    choose_operators=""
    val1=0
    val2=0
    
    decimal=""
    new_val1=0
    new_val2=0

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






'''while True:
    try:
        # create function for calculations 
        def sum(val1,val2):
            return int(val1)+int(val2)
        def sub(val1,val2):
            return int(val1)-int(val2)
        def mul(val1,val2):
            return int(val1)*int(val2)
        def div(val1,val2):
            return int(val1)/int(val2)
        
        # create functions to decimal values
        def sum1(new_val1,new_val2):
            return float(val1)+float(val2)
        def sub1(new_val1,new_val2):
            return float(val1)-float(val2)
        def mul1(new_val1,new_val2):
            return float(val1)*float(val2)
        def div1(new_val1,new_val2):
            return float(val1)/float(val2)

        user=input("Do Your Calculations:-") # for input from users

        # variables for operators and values
        choose_operators=""
        val1=0
        val2=0

        # variables for new operators and values
        decimal=""
        new_val1="0"
        new_val2="0"

        # operators stores in bucket
        operators=["+","-","*","/"]

        
        for i in range(len(user)):
            if (user[i] in operators):
                choose_operators=user[i]
                op=user.index(user[i])
                val1=user[0:op]
                val2=user[op+1:len(user)]

        for i in range(len(val1)):
            if ((val1[i] or val2[i]) == "."):
                new_val1=val1
                new_val2=val2
                
        if ((new_val1 and new_val2) == "0"):
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

        elif ((new_val1 and new_val2) != "0"):
            if choose_operators == "+":
                print("addition:-",sum1(new_val1,new_val2))
            elif choose_operators == "-":
                print("subtract:-",sub1(new_val1,new_val2))
            elif choose_operators == "*":
                print("multiply:-",mul1(new_val1,new_val2))
            elif choose_operators == "/":
                print("division:-",div1(new_val1,new_val2))
            else:
                print("Invalid Choice")

    
    except:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("!sorry")
        print("Give Only Two Numbers for Caculations ! ")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")











    





