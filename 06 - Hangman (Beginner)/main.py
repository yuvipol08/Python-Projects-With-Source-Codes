import random

# Import word list and hangman art
from hangman_words import word_list
from hangman_art import logo, stages

# Choose a word randomly from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize game variables
end_of_game = False
lives = 6

# Display the hangman art logo
print(logo)

# Initialize display with underscores for each letter in the chosen word
display = ["_" for _ in range(word_length)]

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check if the guessed letter is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If guessed letter is not in the word, decrease lives
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    # Check if all letters have been guessed
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Display the current hangman stage
    print(stages[lives])
