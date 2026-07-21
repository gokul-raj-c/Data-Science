# Print a user-entered word in reverse using a while loop (e.g., "python" → "nohtyp"). Do not use slicing.

a=input("enter a word: ")
i=len(a)-1
while i>=0:
    print(a[i],end="")
    i=i-1
