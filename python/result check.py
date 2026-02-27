a=int(input("enter the obtained marks:"));
b="total marks:500"
per=a/5;

print("percentage:",per);


if (a>500):
    print("invalid marks");
    
    
elif (a>=300):
    print("first division");
    print("Congratulations");
    print("Good Job");
    
elif (a>=225):
    print("second division");
    print("Congratulations");
    print("Good");

elif (a>=175):
    print("third division");
    print("Bhagwan Bharose pass hua hai tu....");

elif (a>=150):
    print("result pending......");

else:
    print("fail")

