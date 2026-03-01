class library:
    def __init__(self,name,roll,div):
        self.name=input("enter your name :-")
        self.roll=int(input("enter your rollno:-"))
        self.div=input("your division:-")

    @staticmethod
    def welcome():
        print("Hello Students")
        
s1=library("vikash",4,"ce")
s1.welcome()
s1.welcome()
print("Name:-",s1.name)
print("Roll no:-",s1.roll)
print("Division:-",s1.div)





        
