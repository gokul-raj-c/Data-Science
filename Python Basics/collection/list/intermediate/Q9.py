#Write a menu-driven program using a while loop that repeatedly shows: 
# 1. Add an item 2. Remove last item 3. Display list 4. Exit 
# Use if / elif / else to perform the chosen action on a list. The loop ends only when the user chooses 4.

a=[]
ch=0
while ch!=4:
    print("1.Add an item\n2.Remove last item\n3.Display list\n4.Exit")
    ch=int(input("choose a number: "))
    if ch==1:
        num=int(input("enter value: "))
        a.append(num)
        print("number added")
    elif ch==2:
        if len(a)<=0:
            print("empty list")
        else:
            a.pop()
            print("value deleted from last")
    elif ch==3:
        if len(a)<=0:
            print("empty list")
        else:
            print(a)
    elif ch==4:
        print("exit")
    else:
        print("invalid")
