a=str(input("To Check the vowel,consonent&semi vowel:"))
xlist=["a","e","i","o","u"]
ylist=["w","y"]
if (a in xlist):
    print("vowel")
elif (a in ylist):
    print("semi vowel")
else:
    print("consonent")
