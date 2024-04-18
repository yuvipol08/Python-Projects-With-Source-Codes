from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        # Move the ball
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Bounce the ball vertically
        self.y_move *= -1

    def bounce_x(self):
        # Bounce the ball horizontally
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        # Reset the ball's position to the center and change its horizontal direction
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
