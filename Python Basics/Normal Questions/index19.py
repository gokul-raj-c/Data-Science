#multiple inputs

a,b=input("enter two numbers: ").split(',')
print(a)
print(b)

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

lcm = a
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm = lcm + 1

print("LCM =", lcm)