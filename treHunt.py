print("welcome to treasure Island")
direction=input("Do you want to go left or right?\n")
if direction=="right":
    print("GameOver")
elif direction != "left":
    print("wrong direction")
else:
    mode=input("Do you want to swim or wait?\n")
    if mode == "swim":
        print("Game Over")
    elif mode != "wait":
        print("Wrong mode of transport")
    else:
        door=input("there are three doors. red,blue and green. Choose one?/n")
        if door=="red":
            print("Game Over")
        elif door=="blue":
            print("You Win survived")
        elif door=="green":
            print("death is IDK")
        else:
            print("wrong colour door ra babu.")
