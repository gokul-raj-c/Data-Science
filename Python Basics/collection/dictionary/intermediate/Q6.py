#Reverse the dictionary {"a": 1, "b": 2, "c": 3} so that values become keys and keys become values.

val={
    "a":1,
    "b":2,
    "c":3
}
new={}
a=list(val.keys())
i=0
while i<len(a):
    new[val[a[i]]]=a[i]
    i=i+1
print(val)
print(new)