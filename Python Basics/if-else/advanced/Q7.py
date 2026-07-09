# Rock Paper Scissors

p1=input("choose (rock, paper, or scissors): ")
p2=input("choose (rock, paper, or scissors): ")
if p1==p2:
    print("draw")
elif p1=="rock" and p2=="paper":
    print("Player 2 wins")
elif p1=="rock" and p2=="scissors":
    print("Player 1 wins")
elif p1=="paper" and p2=="rock":
    print("Player 1 wins")
elif p1=="paper" and p2=="scissors":
    print("Player 2 wins")
elif p1=="scissors" and p2=="rock":
    print("Player 2 wins")
elif p1=="scissors" and p2=="paper":
    print("Player 1 wins")
else:
    print("invalid input")