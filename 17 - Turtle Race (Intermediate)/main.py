from turtle import Turtle, Screen
import random

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)

# Get the user's bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Define the colors and starting positions for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-100, -70, -40, -10, 20, 50, 80]

# Create and position the turtles
all_turtles = []
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Start the race if the user has made a bet
is_race_on = False
if user_bet:
    is_race_on = True

# Run the race
while is_race_on:
    for turtle in all_turtles:
        # Check if the turtle has reached the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Move the turtle forward by a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Keep the screen open until clicked
screen.exitonclick()
