f=open("C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\bank.txt","r")
a=f.readlines()
acct_no=input("enter accnt no: ")
pin=input("enter pin: ")
flag=0
for i in range(len(a)):
    details = list(a[i].split("-"))
    if acct_no==details[0] and pin==details[1]:
        print("login success")
        flag=1
        ch=0
        while ch !=5:
            print("1.show balance\n2.deposit\n3.withdraw\n4.pay others\n5.exit")
            ch=int(input("choose a number: "))
            if ch==1:
                print("account balance:",int(details[2]))
                print()
            elif ch==2:
                amt=int(input("enter amount to deposit: "))
                if amt < 0:
                    print("enter valid amount\n")
                else:
                    total=int(details[2])+amt
                    details[2]=str(total)
                    a[i] = "-".join(details) + "\n"
                    f = open("C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\bank.txt", "w")
                    f.writelines(a)
                    print("amount deposited\n")
            elif ch==3:
                amt=int(input("enter amount to withdraw: "))
                if amt < 0:
                    print("enter valid amount\n")
                elif amt > int(details[2]):
                    print("insufficient balance\n")
                else:
                    balance=int(details[2])-amt
                    details[2]=str(balance)
                    a[i] = "-".join(details) + "\n"
                    f = open("C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\bank.txt", "w")
                    f.writelines(a)
                    print("amount debited\n")
            elif ch==4:
                another_user=input("enter account no: ")
                k=0
                for j in range(len(a)):
                    user_details = list(a[j].split("-"))
                    if another_user==user_details[0]:
                        k=1
                        amt=int(input("enter amount: "))
                        if amt < 0:
                            print("enter valid amount\n")
                        elif amt > int(details[2]):
                            print("insufficient balance\n")
                        else:
                            balance=int(details[2])-amt
                            credited=int(user_details[2])+amt
                            details[2] = str(balance)
                            user_details[2] = str(credited)
                            a[i] = "-".join(details) + "\n"
                            a[j] = "-".join(user_details) + "\n"
                            f = open("C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\bank.txt", "w")
                            f.writelines(a)
                            print("amount sent\n")
                            break
                if k==0:
                    print("invalid accnt no\n")
            elif ch==5:
                print("exit")
                break
if flag==0:
    print("login failed")