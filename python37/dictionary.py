data= {1 : "Vikash kumar sharma",
       2 : "Ankur kumar mandal",
       3 : "Ankit kumar sinha",
       4 : "Satyam mishra",
       5 : "Vidya sagar yadav",
       6 : "Ankit kumar sinha",
       7 : "Prem sagar yadav",
       8 : "Roshan kumar mandal",
       "marks" : {
           "phy" : 90,
           "chem" : 80,
           "bio" : 87,
           }

}
print(data["marks"]["chem"])
print(list(data.keys()))
print(list(data.values()))
print(data.get(9)) 

