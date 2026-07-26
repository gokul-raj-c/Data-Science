a=[
    {"name":"gokul","pass":"gokul123","fullname":"gokul raj c","address":"piravom"},
    {"name":"adwaith","pass":"adwaith123","fullname":"adwaith n m","address":"tripunithura"},
    {"name":"allen","pass":"allen123","fullname":"allen albert","address":"thevara"},
    {"name":"nithin","pass":"nithin123","fullname":"nithin mathew thomas","address":"karingachira"},
]

n=input("enter username: ")
p=input("enter password: ")
i=0
f=0
while i<len(a):
    if a[i]["name"]==n and a[i]["pass"]==p:
        print("welcome",a[i]["fullname"])
        print("your address :",a[i]["address"])
        f=1
    i=i+1
if f==0:
    print("invalid username or password")