#Ask the user for a number n. Create a list containing the multiplication table of n from n x 1 to n x 10

n=int(input("enter number: "))
a=[]
i=1
while i<=10:
    a.append(n*i)
    i=i+1
print(a)
