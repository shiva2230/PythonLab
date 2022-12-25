class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        pass
class Book(Publisher):
    def __init__(self,name,title,author):
        Publisher.__init__(self,name)
        self.title=title
        self.author=author
    def display(self):
        pass
class Python(Book):
    def __init__(self,name,title,author,price,noPage):
        Book.__init__(self,name,title,author)
        self.price=price
        self.noPage=noPage
    def display(self):
        print("Name=",self.name)
        print("Title=",self.title)
        print("Author=",self.author)
        print("Price=",self.price)
        print("No of Pages=",self.noPage)

p1=Python("New Publish","Harry Potter","J.K Rowling","500","700")
p1.display()
