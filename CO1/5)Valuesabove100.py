l=[]
n=4

for i in range(n):
    num=int(input("no:"))
    if(num<=100):
        l.append(num)
    else:
        l.append('over') 
print (l)
