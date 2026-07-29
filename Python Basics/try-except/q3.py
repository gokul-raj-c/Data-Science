try:
    a=int(input('enter 1st number: '))
    b=int(input('enter 2nd number: '))
    c=a/b
    print(c)
    x=str(c)
    print(x[5])
except ValueError:
    print("enter integer value")
except ZeroDivisionError:
    print("division by zero")
except IndexError:
    print("string index out of range")
else:    #if try work then else work   if except work else will not work
    print("suiiiii")
finally:
    print("kylian dictator")    #in all cases finally will work