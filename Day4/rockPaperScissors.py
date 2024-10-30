import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

opt = int(input("What do you choose ? Type 0 for Rock, 1 for paper or 2 for Scissors: "))

print(f"You choosed {game_images[opt]}")

computer_opt = random.randint(0, 2)
print(f"Computer choosed {game_images[computer_opt]}")



if opt == 0:
    if computer_opt == 0:
        print("It's a draw")
    elif computer_opt == 1:
        print("You lose")
    elif computer_opt == 2:
        print("You win")
elif opt == 1:
    if computer_opt == 0:
        print("You lose")
    elif computer_opt == 1:
        print("It's a draw")
    elif computer_opt == 2:
        print("You win")
elif opt == 2:
    if computer_opt == 0:
        print("You lose")
    elif computer_opt == 1:
        print("You win")
    elif computer_opt == 2:
        print("It's a draw")
else:
    print("Invalid option")