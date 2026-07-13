#Make a simple menu program. Repeatedly show:
    #1. Say Hello
    #2. Say Bye
    #3. Exit
#Use a while loop with if / elif / else to respond to the user's choice. The loop only ends when they choose 3

c=0
while c!=3:
    print("1.say hello\n2.say bye\n3.exit")
    c=int(input("choose a number:"))
    if c==1:
        print("hello\n")
    elif c==2:
        print("bye\n")
    elif c==3:
        print("exit\n")
    else:
        print("invalid number\n")