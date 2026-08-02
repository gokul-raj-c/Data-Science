#From ("anu", "harini", "ravi", "meera") , find the longest name without sorting the tuple

a=("anu", "harini", "ravi", "meera")
long=a[0]
for i in a:
    if len(long)<len(i):
        long=i
print(a)
print(long)
