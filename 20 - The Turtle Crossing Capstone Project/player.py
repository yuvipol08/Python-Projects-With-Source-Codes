from turtle import Turtle

# Define constant values for the player
STARTING_POSITION = (0, -280)  # Starting position of the player
MOVE_DISTANCE = 10  # Distance the player moves up
FINISH_LINE_Y = 280  # Y-coordinate of the finish line


# A class to represent the player turtle
class Player(Turtle):
    # Initialize the player
    def __init__(self):
        super().__init__()
        self.shape("turtle")  # Set the shape of the player to a turtle
        self.penup()  # Lift the pen to prevent drawing
        self.go_to_start()  # Move the player to the starting position
        self.setheading(90)  # Set the orientation of the player to face north

    # Move the player upwards
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # Move the player to the starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Check if the player has reached the finish line
    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
