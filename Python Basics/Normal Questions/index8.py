print("start")
a=10
x=5
if a>20:
    #indendation
    #print('positive')
    x=x*10
elif a>0:
    #print('negative')
    x=x*20
elif a>9:
    print("suuiii")
else:
    #conditions that are not held by if and elif are taken here, here no condition is checked
    #print('zero')
    x=x-5
print('stop')
print(x)