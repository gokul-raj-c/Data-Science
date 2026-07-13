#Write a small number-guessing game. The secret number is 7. Keep asking the user to guess. Print "Too high" or "Too low", and stop when they guess correctly

n=0
while n!=7:
    n=int(input("enter secret number: "))
    if n<7:
        print("too low")
    elif n>7:
        print("too high")
    else:
        print("found it")