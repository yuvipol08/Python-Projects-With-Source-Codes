import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player, car manager, and scoreboard objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for player input
screen.listen()
screen.onkey(player.go_up, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    # Pause the game for a short duration
    time.sleep(0.1)
    # Update the screen
    screen.update()

    # Create cars and move them
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

# Exit the game on click
screen.exitonclick()
