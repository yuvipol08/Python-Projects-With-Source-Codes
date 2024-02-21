# Print an ASCII art of a treasure island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |  __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************
''')

# Print a welcome message
print("Welcome to Treasure Island.")
print("Your Mission is to find the treasure")

# Get the user's first choice
choice1 = input("You are at a crossroad. Where do you want to go? Type \"left\" or \"right\": ").lower()

# Check the user's first choice
if choice1 == "left":
    # Get the user's second choice
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. "
                    "Type \"wait\" to wait for a boat or Type \"swim\" to swim across: ").lower()

    # Check the user's second choice
    if choice2 == "wait":
        # Get the user's third choice
        choice3 = input("You have arrived at the island unharmed. There is a house with 3 doors. "
                        "One Red, one Blue, and one Green. Which color do you choose? ").lower()

        # Check the user's third choice
        if choice3 == "red":
            print("You found the treasure! You Won!")
        elif choice3 == "blue":
            print("You entered a room of beasts! Game Over!")
        elif choice3 == "green":
            print("You entered a room of snakes! Game Over!")
        else:
            print("You chose a door that does not exist! Game Over!")
    else:
        print("You are attacked by trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")
