import random
folder="C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\hospital\\"

is_registered=input("Registered Yes/No: ")
if is_registered=="Yes":
    reg_no=input("enter register no: ")
    file=folder+reg_no+".txt"
    try:
        f=open(file,"r")
        a=f.read()
        print(a)
    except FileNotFoundError:
        print("Register number incorrect")
else:
    flag=0
    while flag==0:
        reg_no_new=random.randint(100,1000)
        new_file=folder+str(reg_no_new)+".txt"
        try:
            f=open(new_file,"r")
        except FileNotFoundError:
            f=open(new_file,"x")
            name=input("enter name: ")
            age=input("enter age: ")
            address=input("enter address: ")
            f.write("Name: "+name+"\n")
            f.write("Age: "+age+"\n")
            f.write("Address: "+address)
            print("user registered with reg no:",reg_no_new)
            flag=1