while True:
    a=int(input("to check the prime number:-"))
    if (a<2):
        print(f"{a} is not prime")

    for i in range(2,(a//2)+1):
        
        if (a%i==0):
            print(f"{a} is not prime")
            break
    else:
        print(f"{a} is prime no")
            
