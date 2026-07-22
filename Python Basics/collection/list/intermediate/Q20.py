#A list marks= [78,45,92,60,33] stores student marks. Using a while loop with if / elif / else,
#  print the grade for each mark: 
# 90 and above: "A" 
# 75 to 89: "B" 
# 60 to 74: "C" 
# 40 to 59: "D" 
# Below 40: "Fail" 
# Also print how many students passed (40 and above).

a=[78,45,92,60,33]
i=0
c=0
while i<len(a):
    if a[i]>=90:
        print("A")
        c=c+1
    elif a[i]>=75 and a[i]<90:
        print("B")
        c=c+1
    elif a[i]>=60 and a[i]<75:
        print("C")
        c=c+1
    elif a[i]>=40 and a[i]<60:
        print("D")
        c=c+1
    else:
        print("fail")
    i=i+1
print("no of students passed (40 and above):",c)