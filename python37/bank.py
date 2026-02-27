class bank:
    def __init__(self,bank_account):
        self.account=bank_account

    def costumer(self,ac_no,name,branch,IFSC,bal):
        self.ac=ac_no
        self.name=name
        self.branch=branch
        self.ifsc=IFSC
        self.bal=bal

    def details(self,data):
        self.data= {
    "account_no":[123456789101,
                  123456789102,
                  123456789103,
                  123456789104,
                  123456789105,
                  123456789106,
                  123456789107,
                  123456789108,
                  123456789109,
                  123456789110],
    
    "name": [ "Vikash kumar sharma",
            "Ankur kumar mandal",
            "Ankit kumar sinha",
            "Ankit kumar sinha",
            "Ankit kumar sinha",
            "Satyam mishra",
            "Vidya sagar yadav",
            "Ankit kumar sinha",
            "Prem sagar yadav",
            "Roshan kumar mandal",],
    
    "balance":[100021,
               100212,
               121126,
               521001,
               587001,
               424100,
               875672,
               572656,
               628659,
               528262
               ]
    }
        print(data["account_no"][0])

        return self.data

    def debit(self,debit):
        self.debit=int(input("how much debit rs:-"))
        
        
        


        

s1=bank("State Bank of India")
print(s1.account)
s1.details("data")
print(s1.details("data"))
        
