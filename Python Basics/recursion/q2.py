def home(a):
    if a==0:
        return 1
    return a*home(a-1)
x=home(4)
print(x)