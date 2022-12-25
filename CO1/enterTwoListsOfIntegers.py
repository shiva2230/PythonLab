list1=[]
list2=[]
sum1=0
sum2=0
n1=int(input("Enter how many numbers in first list:\n"))
for i in range(n1):
    num=int(input("no."))
    sum1=sum1+num;
    list1.append(num)
n2=int(input("Enter how many numbers in second list:\n"))
for i in range(n2):
    num=int(input("no."))
    sum2=sum2+num;
    list2.append(num)
if(len(list1)==len(list2)):{
    print("Lists are of same length")
    }
else:
    print("Lists arent of same length")
if(sum1==sum2):{
    print("Sum of elements of both lists are equal")
    }
else:
    print("Sum of elements of both lists are not equal")
occ=set(list1).intersection(list2)
if(occ==None):
    print("No common value")
else:
    print("The occurences in the list are",occ)

print("List1 = ",list1)
print("List2 = ",list2)
