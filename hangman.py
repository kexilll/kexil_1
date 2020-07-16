#hangman_project_6/28/2020 Ke

step=["|--------        ",
      "|       |        ",
      "|       O        ",
      "|     / | \      ",
      "|       |        ",
      "|     /   \      "]

wrong=0
chance=6
print("Welcome to the Hangman game")

pl1=input("Enter a word that you want player 2 to guess")
board=["-"]*len(pl1)
pl1=list(pl1)

for i in range(100):
    print("Game start!")
print()
print("".join(board))

while wrong<len(step):
    print()
    pl2=input("Guess a letter!")

    result=pl2 in pl1

    if result is True:
        ca=pl1.index(pl2)
        board[ca]=(pl2)
        pl1[ca]=("@")
        

    else:
        print ("Wrong!")
        wrong= wrong+1
    
    print()
    print(''.join(board))
    print()
    print("\n".join(step[0:wrong]))
    if "-" not in board:
        break

if "-" not in board:
    print("love You LuLu!")
else:
    print("Try again!")
