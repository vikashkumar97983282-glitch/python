list=["a","e","i","o","u"]
list1=["w","y"]
while True:
    print("To check the vowel,consonent & semivowel")
    x=str(input("enter the value:"))
    if x is str:
        pass
    y=x.lower()
    if y in list:
        print("#### vowel ####")
    elif y in list1:
        print("####semivowel####")
    else:
        print("####consonent####")
