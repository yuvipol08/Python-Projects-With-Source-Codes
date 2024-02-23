import random

# ASCII art for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of game images
game_images = [rock, paper, scissors]

# Get user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))

# Check if the user's choice is valid
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, You lose!")
else:
    # Print the user's choice
    print(game_images[user_choice])

    # Generate computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the winner
    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You Win")
    elif computer_choice == user_choice:
        print("It's a draw!")
