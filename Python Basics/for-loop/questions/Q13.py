#Count the number of vowels in a string.

s=input("enter string: ")
print(s)
c=0
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        c=c+1
print(c)

# vowels=["a","e","i","o","u"]
# s=input("enter string: ")
# print(s)
# c=0
# for i in s:
#     if i in vowels:
#         c=c+1
# print(c)

