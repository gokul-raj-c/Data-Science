#Ask the user to enter 5 numbers and count how many were positive and how many were negative.

c_pos=0
c_neg=0
i=1
while i<=5:
    a=int(input("enter number: "))
    if a<0:
        c_neg=c_neg+1
    if a>0:
        c_pos=c_pos+1
    i=i+1
print("count of positive numbers:",c_pos)
print("count of negative numbers:",c_neg)