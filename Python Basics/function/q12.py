#Write a function times_table(n) that prints the multiplication table of n from 1 to 10, one line per row (e.g. 7 x 3 = 21).

def times_table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

num=int(input("enter number: "))
times_table(num)