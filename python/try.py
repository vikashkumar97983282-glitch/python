questions=[]
answer_key=[]

a=int(input("enter the no of questions:-"))

while True:
    for i in range(0,a):
        #questions.append[i]
        q=input(f"enter the questions{i+1} :-")
        questions.append([q])
        for j in range(1,5):
            q=input(f"enter the options{j}:-")
            questions[i].insert(j,q)  #adding element specific index
        key=int(input(f"answer key{i+1}:-"))
        answer_key.append(key)
    print(questions)
    print(answer_key)

    print("########################################################################")

    for k in range(0,len(questions)):
        print(f"Q.no.{k+1}  {questions[k][0]}")
        print(f" 1. {questions[k][1]}   2. {questions[k][2]}")
        print(f" 3. {questions[k][3]}   4. {questions[k][4]}")

        choose=int(input("choose your answer:-"))
        if choose == answer_key[k]:
            print("correct answer")
        else:
            print("wrong answer")

        try: 
            query=input("if set you new query(yes/no):-")
            if query == yes:
                continue
            else:
                break
        except:
            print("please enter valid reason.")
        

