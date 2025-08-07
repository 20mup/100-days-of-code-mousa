import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!\n")

# Safe input capture
choice_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# Validate before converting or using
if not choice_input.isdigit():
    print("Invalid input. You lose!")
else:
    choice = int(choice_input)
    
    if choice < 0 or choice > 2:
        print("You typed an invalid number. You lose!")
    else:
        print(f"\nYou chose:\n{game_images[choice]}")
        
        computer_choice = random.randint(0, 2)
        print(f"\nComputer chose:\n{game_images[computer_choice]}\n")

        if choice == computer_choice:
            print("It's a draw!")
        elif (choice == 0 and computer_choice == 2) or \
             (choice == 1 and computer_choice == 0) or \
             (choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")
