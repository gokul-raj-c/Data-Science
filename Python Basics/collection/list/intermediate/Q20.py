#A list marks= [78,45,92,60,33] stores student marks. Using a while loop with if / elif / else,
#  print the grade for each mark: 
# 90 and above: "A" 
# 75 to 89: "B" 
# 60 to 74: "C" 
# 40 to 59: "D" 
# Below 40: "Fail" 
# Also print how many students passed (40 and above).

marks=[78,45,92,60,33]
i=0
c=0
while i<len(marks):
    if marks[i]>=90:
        print(marks[i],"-> A")
        c=c+1
    elif marks[i]>=75:
        print(marks[i],"-> B")
        c=c+1
    elif marks[i]>=60:
        print(marks[i],"-> C")
        c=c+1
    elif marks[i]>=40:
        print(marks[i],"-> D")
        c=c+1
    else:
        print(marks[i],"-> Fail")
    i=i+1
print("no of students passed (40 and above) =",c)
