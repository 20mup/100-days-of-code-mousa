# Day 3 Project: Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ 
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the hidden treasure!\n")

choice1 = input("You're at a crossroad.\nWhere do you want to go? Type 'left' or 'right':\n").lower()

if choice1 == "left":
    print("You get to live for now...\n")
    choice2 = input("You reach a wide river.\nWill you 'wait' for a boat or 'swim' across?\n").lower()
    
    if choice2 == "wait":
        print("A wise decision. A boat takes you safely across.\n")
        choice3 = input("On the island, you find a house with 3 doors: one red, one yellow, and one blue.\nWhich do you choose?\n").lower()
        
        if choice3 == "yellow":
            print("Yellow must be your lucky color. You found the treasure! You win! 🏆")
        elif choice3 == "red":
            print("You open the red door and step into a room full of fire. Game over. 🔥")
        elif choice3 == "blue":
            print("You walk into a room full of beasts. Game over. 🐺")
        else:
            print("You chose a door that doesn’t exist. Game over. 🤷")
    
    elif choice2 == "swim":
        print("You're not a very smart fella. A trout drags you under. Game over. 🐟")
    else:
        print("I don't think you understand how this works. Game over.")
        
elif choice1 == "right":
    print("You fall into a hole immediately. Game over. 🕳️")
else:
    print("Invalid input. You wander off and are never seen again. Game over.")
