import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",password="goookul8393#",database="atm")
print(connection.is_connected())

cursor=connection.cursor(dictionary=True)   

f1=0
while f1 != 1:
    print("------Bank------")
    accnt_no=int(input("enter account no: "))
    pin_no=int(input("enter pin no: "))
    print()
    query="select * from accounts where accnt_no = %s and pin = %s "
    cursor.execute(query,(accnt_no,pin_no))
    data=cursor.fetchone()
    if data:
        print(f"Welcome {data['user_name']}")
        f2=0
        while f2 != 4:
            print("1.Show Balance\n2.Deposit Amount\n3.Withdraw Amount\n4.Exit\n")
            f2=int(input("choose one option: "))
            match(f2):
                case 1:
                    print(f"Your Current Balance: {data['balance']} Rs\n")

                case 2:
                    amt=int(input("Enter Amount to Deposit: "))
                    query="update accounts set balance=balance + %s where accnt_no=%s"
                    cursor.execute(query,(amt,accnt_no))
                    connection.commit()
                    print(f"₹{amt} Deposited Successfully")
                    query = "SELECT balance FROM accounts WHERE accnt_no = %s"
                    cursor.execute(query, (accnt_no,))
                    data = cursor.fetchone()
                    print(f"Your Current Balance: {data['balance']} Rs\n")

                case 3:
                    amt=int(input("Enter Amount to Withdraw: "))
                    query = "SELECT balance FROM accounts WHERE accnt_no = %s"
                    cursor.execute(query, (accnt_no,))
                    data = cursor.fetchone()
                    if amt > data['balance']:
                        print("Invalid Balance\n")
                    else:
                        query="update accounts set balance=balance - %s where accnt_no=%s"
                        cursor.execute(query,(amt,accnt_no))
                        connection.commit()
                        print(f"₹{amt} Withdrawed Successfully")
                        query = "SELECT balance FROM accounts WHERE accnt_no = %s"
                        cursor.execute(query, (accnt_no,))
                        data = cursor.fetchone()
                        print(f"Your Current Balance: {data['balance']} Rs\n")

                case 4:
                    print("Thank You !\n")
                    break

                case _:
                    print("Enter Valid Input")

    else:
        print("Invalid Username or Pin no\n")