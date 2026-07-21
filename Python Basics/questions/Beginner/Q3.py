#Ask the user for two numbers (start and end) and print the sum of only the numbers between them that are divisible by 3.

start=int(input("enter starting number: "))
end=int(input("enter ending number: "))
s=0
while start<=end:
    if start%3==0:
        s=s+start
    start=start+1
print(s)