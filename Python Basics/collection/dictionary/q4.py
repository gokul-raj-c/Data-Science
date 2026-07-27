bank=[
    {"name":"gokul","password":"gokul123","balance":3000,"phoneno":9061393951},
    {"name":"adwaith","password":"adwaith123","balance":3000,"phoneno":9234561201},
    {"name":"allen","password":"allen123","balance":3000,"phoneno":8212078856},
    {"name":"thomas","password":"thomas123","balance":3000,"phoneno":9217632900},
    {"name":"nithin","password":"nithin123","balance":3000,"phoneno":8144810023},
]

n=input("enter username: ")
p=input("enter password: ")
i=0
f=0
while i<len(bank):
    if bank[i]["name"]==n and bank[i]["password"]==p:
        f=1
        print("\nwelcome")
        ch=1
        while ch!=5:
            print("1.show balance\n2.deposit amount\n3.withdraw amount\n4.send amount to a number\n5.exit\n")
            ch=int(input("choose a number: "))
            if ch==1:
                print("your balance:",bank[i]["balance"])
                print()
            elif ch==2:
                dep=int(input("enter amount: "))
                bank[i]["balance"]=bank[i]["balance"]+dep
                print("amount deposited\n")
            elif ch==3:
                withdraw=int(input("enter amount: "))
                if withdraw <= bank[i]["balance"]:
                    bank[i]["balance"]=bank[i]["balance"]-withdraw
                    print("amount debited from account\n")
                else:
                    print("insufficient balance\n")
            elif ch==4:
                num=int(input("enter number of user: "))
                j=0
                flag=0
                while j<len(bank):
                    if bank[j]["phoneno"]==num and bank[i]["phoneno"] !=num:
                        flag=1
                        print("send money to:",bank[j]["name"])
                        print()
                        amt=int(input("enter amount to send: "))
                        if amt > bank[i]["balance"]:
                            print("insufficient balance\n")
                        else:
                            bank[i]["balance"]=bank[i]["balance"]-amt
                            bank[j]["balance"]=bank[j]["balance"]+amt
                            print("amount send\n")
                    j=j+1
                if flag==0:
                    print("no user found in this number\n")
            elif ch==5:
                print("exit")
            else:
                print("invaid number\n")
    i=i+1
if f==0:
    print("invalid username or password")