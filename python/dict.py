dict={"Vikash":41,
      "Ashif":42,
      "Gaurav":43,
      "Rahul":44,
      "Raj":45
      }
while True:
    try:
        print("search your student rollno")
        a=input("enter student name:")
        b=a.capitalize()
        print(dict[b])
    except:
        print("Invalid! enter the valid name")
