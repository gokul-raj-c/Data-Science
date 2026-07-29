i=True
while i==True:
    try:
        a=int(input("enter number: "))
        i=False
        print(a)
    except:
        print("enter integer value")
        i=True
