#Restaurant Bill

t=int(input("enter total bill: "))
is_member=input("is customer a member(yes/no): ")
amt=t+(t*0.05)
if amt>2000:
    amt=amt+(amt*0.10)
if is_member=="yes":
    amt=amt-100
print("total amount:",amt)