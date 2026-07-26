# Two sets store students who passed math and science: {1, 2, 3, 5} and {2, 3, 4, 5}. Find the students who passed both subjects.

a={1,2,3,5}
b={2,3,4,5}


x=list(a)
y=list(b)
i=0
while i<len(x):
    j=0
    while j<len(y):
        if x[i]==y[j]:
            print(x[i])
        j=j+1
    i=i+1

# for x in a:
#     if x in b:
#         print(x)
