#Reverse a string using a for loop

s="gokul"
y=""
for i in range(len(s)-1,-1,-1):
    y=y+s[i]
print(s)
print(y)