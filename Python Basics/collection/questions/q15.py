#From the names "harini" and "kiran" , print the letters found in both names and the letters found in only one of them.

w1="harini"
w2="kiran"
a=set(w1)
b=set(w2)
print("letters found in both names:",(a&b))
print("the letters found in only one of them:",(a^b))