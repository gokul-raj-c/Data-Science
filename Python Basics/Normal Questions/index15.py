a=int(input("enter number: "))
if a%60==0:
    if a%30==0:
        if a%15==0:
            if a%5==0:
                if a%3==0:
                    print("pass every divisible test")
                else:
                    print("not divisible by 60")
            