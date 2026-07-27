#Ask the user to enter names until they type "stop". Store unique names in a set and print the final set.

names=set()
n=""
while n!="stop":
    n=input("enter name: ")
    if n!="stop":
        names.add(n)
print(names)