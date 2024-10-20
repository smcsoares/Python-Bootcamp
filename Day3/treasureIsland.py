print('''Welcome to Treasure Island. 
      Your mission is to find the treasure''')

left_right = input("left or right ?").lower()

if left_right == "right":
    print("Game Over")
elif left_right == "left":
    swim_wait = input ("swim or wait ?").lower()
    if swim_wait == "swim":
        print("Game Over")
    elif swim_wait == "wait":
        door = input("Which door ? blue, red or yellow ?").lower()
        if door == "red" or door == "blue":
            print("Game Over")
        elif door == "yellow":
            print("You win")
        else:
            print("Invalid input") 
    else:
        print("Invalid input")    
else:
    print("Invalid input")
