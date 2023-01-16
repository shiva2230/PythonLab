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
        

    def showBal(self):
        print("Total available balance=",self.bal)

        
bal=0
choice=0
accNum=input("Enter the name:")
accNo=int(input("Enter your account number:"))
accType=input("Enter your account type:")
cust1=Bank(accNum,accNo,accType,bal)
while(choice!=4):
    choice=int(input("Enter your choice: \n1. Deposit\n2.Withdraw\n3.Check Balance\n4.Exit"))

    if(choice==1):
        depAmt=int(input("Enter how much amount you want to deposit\n"))
        cust1.deposit(depAmt)
    elif(choice==2):
        withAmt=int(input("Enter how much amount you want to withdraw\n"))
        cust1.withdraw(withAmt)
    elif(choice==3):
        cust1.showBal()



        
