
def prime(num):
    if (num<=1):
        print("a")
    for i in range(2,num):
        if (num % i == 0):
        
            return 0
    return 1

num = int(input("enter the number:-"))

if (prime(num)==0):
    print("non prime")
else:
    print("prime")

