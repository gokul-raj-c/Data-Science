# ATM Withdrawal

bal = int(input("enter account balance: "))
amt = int(input("enter withdraw amount: "))

if amt % 100 != 0:
    print("Enter multiples of 100")
elif amt > bal:
    print("Insufficient funds")
else:
    bal = bal - amt
    print("Remaining balance:", bal)