f=open("C:\\Users\\Gokul\\OneDrive\\Desktop\\Suii\\bank.txt","r")
a=f.readlines()
acct_no=input("enter accnt no: ")
pin=input("enter pin: ")
f=0
for i in a:
    details=list(i.split("-"))
    if acct_no==details[0] and pin==details[1]:
        print("login success")
        f=1
        ch=0
        while ch !=4:
            print("1.show balance\n2.deposit\n3.withdraw\n4.exit")
            ch=int(input("choose a number: "))
            if ch==1:
                print("account balance:",int(details[2]))
                print()
            elif ch==2:
                amt=int(input("enter amount to deposit: "))
                total=int(details[2])+amt
                details[2]=str(total)
                print("amount deposited\n")
            elif ch==3:
                amt=int(input("enter amount to withdraw: "))
                if amt > int(details[2]):
                    print("insufficient balance\n")
                else:
                    balance=int(details[2])-amt
                    details[2]=str(balance)
                    print("amount debited\n")
            elif ch==4:
                print("exit")
                break
if f==0:
    print("login failed")
    
    