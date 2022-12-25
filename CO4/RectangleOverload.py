class Rectangle:
    def __init__(self,l,b):
        self.__l=l
        self.__b=b
        self.area=self.__l*self.__b
        
    def __lt__(self,other):
       return self.area < other.area


 
a = int(input("Enter length of first rectange : "))
b = int(input("Enter width of first rectangle : "))
c = int(input("Enter length of second rectangle : "))
d = int(input("Enter width of second rectangle : "))


rect1 = Rectangle(a,b)
rect2 = Rectangle(c,d)

if(rect1<rect2):
    print("Rectangle 2 is greater")
else:
    print("Rectangle 1 is greater")
    

