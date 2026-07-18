list=[1]
n=int(input("enter the value of n"))
for i in list:
    while i<n:
        list.append(i+2)
        break
print (list)