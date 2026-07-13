#Ask the user to enter numbers one by one. Keep a running total, and stop when the total becomes greater than 50. Print how many numbers were entered

c=0
s=0
while s<=50:
    n=int(input("enter number: "))
    s=s+n
    c=c+1
print("count of numbers entered:",c)