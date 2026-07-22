#Write a linear search program. Ask the user for a number, search the list [11, 24,36,47,58], and print the index where it was found, 
# or -1 if it is not present.

a=[11, 24,36,47,58]
b=int(input("enter number: "))
i=0
f=0
while i<len(a):
    if a[i]==b:
        f=1
        print("found at index:",i)
    i=i+1
if f==0:
    print(-1)