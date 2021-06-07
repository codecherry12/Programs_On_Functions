class ISFE(Exception):
    def __init__(self,m):
        self.dm=m

class Account():
    def __init__(self,n,b):
        self.AccountNumber=n
        self.Balance=b
    def withdraw(self,amt):
        b=self.Balance-amt
        if b<1000:
            raise ISFE("1000 is min balance...")
        self.Balance=self.Balance-amt
    def __str__(self):
        return "AccountNumber is {}, and Balance is {}".format(self.AccountNumber,self.Balance)



a1=Account(101,2000)
print(a1)
try:
    a1.withdraw(2500)
except ISFE as e:
    print(e)
print(a1)
