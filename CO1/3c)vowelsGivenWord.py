s=input("Enter the words\n")
list=[]
for x in s:
    if x  in ('a','e','i','o','u'):
        list.append(x)
print(list)
