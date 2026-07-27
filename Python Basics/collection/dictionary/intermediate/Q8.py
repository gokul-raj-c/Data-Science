#. Make a simple phone book menu using a while loop. The menu should allow the user to add a contact, 
# search for a contact, display all contacts, and exit

contacts={
    "gokul":9061393951,
    "adwaith":9832401634,
    "thomas":8713468290,
}
n=1
while n!=4:
    print("1.add contact\n2.search contact\n3.display all contact\n4.exit")
    n=int(input("choose: "))
    if n==1:
        name=input("enter name: ")
        num=int(input("enter number: "))
        contacts[name]=num
        print("number added")
    elif n==2:
        val=input("enter name: ")
        k=list(contacts.keys())
        i=0
        f=0
        while i<len(k):
            if k[i]==val:
                f=1
                print("name:",val)
                print("no:",contacts[k[i]])
            i=i+1
        if f==0:
            print("not found")
    elif n==3:
        k=list(contacts.keys())
        if len(k)==0:
            print("no contacts")
        else:
            i=0
            while i<len(k):
                print("Name:",k[i],"Phone No:",contacts[k[i]])
                i=i+1
    elif n==4:
        print("exit")
    else:
        print("invalid")
    