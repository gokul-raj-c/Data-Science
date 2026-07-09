# Loan Eligibility

a=int(input("enter age: "))
i=int(input("enter income: "))
cs=int(input("enter credit score: "))
if a>=21 and a<=60:
    if i>=25000:
        if cs>=700:
            print("loan approved")
        else:
            print("loan rejected")
    else:
        print("loan rejected")
else:
    print("loan rejected")