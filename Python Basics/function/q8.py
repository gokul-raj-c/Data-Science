#Write a function that returns the larger of two numbers.

def find_larger(a,b):
    if a>b:
        print("large:",a)
    else:
        print("large:",b)

x=int(input("enter 1st number: "))
y=int(input("enter 2nd number: "))
find_larger(x,y)