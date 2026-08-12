folder="C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\"
num=input("enter phone number: ")
file=folder+num+".txt"
try:
    f=open(file,"r")
    a=f.read()
    print(a)
except FileNotFoundError:
    name=input("enter name: ")
    age=input("enter age: ")
    address=input("enter address: ")
    f=open(file,"w")
    f.write("name: " + name + "\n")
    f.write("age: " + age + "\n")
    f.write("address: " + address)