from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()




'''list=[]
num=int(input("enter the number of person you want to enter :"))
for i in range(1,num+1):
    print("the name of person ",i,":",end=" ")
    name= input()
    a=list.append(name)
print(list)
while True:
  b=input("\ndo you want to remove any name (y/n):")
  if b=="y":
    c=input("name:")
    list.remove(c)
    print(list)'''




