#Ask the user for a number n. Using a using a while loop, create a list 
# containing the multiplication table of n (n x 1 to n x 10) and print it.

n=int(input("enter number: "))
a=[]
i=1
while i<=10:
    a.append(n*i)
    i=i+1
print(a)