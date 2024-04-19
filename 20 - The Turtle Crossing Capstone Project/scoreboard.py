from turtle import Turtle

# Define the font style for the scoreboard
FONT = ("Courier", 24, "normal")


# A class to represent the scoreboard
class Scoreboard(Turtle):

    # Initialize the scoreboard
    def __init__(self):
        super().__init__()
        self.level = 1  # Initialize the level to 1
        self.hideturtle()  # Hide the turtle icon
        self.penup()  # Lift the pen to prevent drawing
        self.goto(-280, 250)  # Position the scoreboard
        self.update_scoreboard()  # Update the scoreboard with the initial level

    # Update the scoreboard with the current level
    def update_scoreboard(self):
        self.clear()  # Clear the previous content
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the current level

    # Increase the level by 1 and update the scoreboard
    def increase_level(self):
        self.level += 1  # Increment the level by 1
        self.update_scoreboard()  # Update the scoreboard with the new level

    # Display 'GAME OVER' message at the center of the screen
    def game_over(self):
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align="center", font=FONT)  # Write 'GAME OVER'
