import random
print("Welcome to the game")

options=["Rock","Paper","Scissors"]
Player1=options[int(input("what do you choose? 0-Rock,1-Paper,2-Scissors"))]
print(f"Player1 Chose {Player1}")
AiChoose=options[random.randint(0,2)]
print(f"AI choose {AiChoose}")

if Player1==AiChoose:
    print("Its a tie")
elif (Player1 == "Rock" and AiChoose == "Scissors") or \
     (Player1 == "Scissors" and AiChoose == "Paper") or \
     (Player1 == "Paper" and AiChoose == "Rock"):
         print("You win!")
else:
     print("Computer wins!")