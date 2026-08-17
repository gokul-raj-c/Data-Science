def home(a):
    if a==25:
        return
    print(a)
    home(a+1)
    print("hi")
home(20)

#output
# 20
# 21
# 22
# 23
# 24
# hi
# hi
# hi
# hi
# hi