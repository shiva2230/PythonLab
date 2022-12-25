sum=0
l=[]
n=int(input("Enter the limit"))
print("Enter the elements:")
for i in range(n):
    num=int(input())
    l.append(num)
print(l)
for i in range (0,len(l)):
    sum=sum+l[i]
print("Sum of all elements in the list",sum)    
