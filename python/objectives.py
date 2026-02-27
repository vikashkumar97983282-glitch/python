# ####### QUIZ ######
questions=[ ["who is the persident of india ?","narendra modi","dropadi murmu","rahul gandhi","amit shah"],
   ["who is the prime minister of india ?","narendra modi","rahul gandhi","amit shah","dropadi murmu"],
   ["who is the chief minister of bihar ?","Nitish Kumar","Lalu yadav","Chirag Paswan","Anand Kishore"],
   ["Where is the capital of INDIA ?","Mumbai","Kolkata","Bihar","New Delhi"]
]

ans=[2,1,1,4]
# point=[5,10,15,20]
cr=0

while True:
    for i in range(0,len(questions)):
      question = questions[i]
      print(" ")
      print(i+1,question[0])
      print(f"  1. {question[1]}  2. {question[2]}" )
      print(f"  3. {question[3]}  4. {question[4]}" )
      ch=int(input("choose your answer (1-4) :"))
      if ch==ans[i]:
        cr=cr+5
        print(f"correct answer ! you won {cr} points")
      else:
        print(f"wrong answer! you have {cr} points")
        a=input("\nDo you want try another questions (y/n) :")
        if a=="y":
          continue
        else:
          break
    print(f"\nYour Total points is {cr}")
    print(f"percentage is {cr*100/20}")
    if cr<=50:
        print("you qualified")
    else:
        print("you are failed")
    attemp=input("\n\nTry another attempt (y/n):")
    if attemp=="y":
        continue
    else:
        break
