class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def displayArea(self):
        print("Area=",(self.l*self.b))

    def displayPeri(self):
        print("Perimeter=",2*(self.l+self.b))

    def returnArea(self):
        return (self.l*self.b)
    
    #def returnPeri(self):
     #   return 2*(self.l*self.b)
    
r1=Rectangle(5,3)
r2=Rectangle(4,6)
r1.displayArea()
r2.displayArea()
r1.displayPeri()
if r1.returnArea()>r2.returnArea():
    print("r1 is greater")
else:
    print("r2 is greater")
