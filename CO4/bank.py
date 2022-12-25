class Bank:
    def __init__(self,name,accNo,accType,bal):
        self.name=name
        self.accNo=accNo
        self.accType=accType
        self.bal=bal

    def deposit(self,depAmt):
        self.depAmt=self.bal+depAmt
        print("Amount deposited: ",depAmt)
        self.bal=self.bal+depAmt
        print("Total available balance=",self.bal)
        
    def withdraw(self,withAmt):
        self.withAmt=self.bal-withAmt
        print("Amount withdrawn: ",withAmt)
        self.bal=self.bal-withAmt
        print("Total available balance=",self.bal)
        

    def showBal():
        print("Total available balance=",self.bal)

        
bal=0

accNum=input("Enter the name:")
accNo=input("Enter your account number:")
accType=input("Enter your account type:")
cust1=Bank(accNum,accNo,accType,bal)
cust1.deposit(100)
cust1.withdraw(53)
cust1.deposit(100)
#cust1.showBal()
        
