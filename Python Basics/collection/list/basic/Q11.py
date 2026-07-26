#Ask the user to enter 5 numbers one by one.Store them in a list and print the final list.

a=[]
i=1
while i<=5:
    b=int(input("enter number: "))
    a.append(b)
    i=i+1
print(a)