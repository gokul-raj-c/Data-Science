#A dictionary stores votes: {"A": 4, "B": 4, "C": 2}. Check whether there is a tie for the highest vote count

votes={
    "A":4,
    "B":4,
    "C":2
}
print(votes)
a=list(votes.keys())
high=votes[a[0]]
i=1
while i<len(a):
    if votes[a[i]]>high:
        high=votes[a[i]]
    i=i+1
count=0
i=0
while i<len(a):
    if votes[a[i]]==high:
        count=count+1
    i=i+1
if count>1:
    print("tie")
else:
    print("no tie")
