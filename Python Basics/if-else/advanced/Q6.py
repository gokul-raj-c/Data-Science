#Movie Ticket with Day Discount

a = int(input("enter age: "))
d = input("enter day: ")
p = 250
if d == "Wednesday":
    p = p / 2
if a < 12 or a >= 60:
    p = p - 50
print("Ticket price:", p)