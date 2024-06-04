import turtle

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()

    def show_score(self):
        self.pen.clear()
        self.pen.goto(0, 0)  # Position the pen at the center (or any desired position)
        self.pen.write(arg=f"Score: {self.score}", move=True, align="center", font=('Arial', 8, 'normal'))

    def increase_score(self):
        self.score += 1
        self.show_score()

# Example of how this class can be used
screen = turtle.Screen()
screen.title("Scoreboard Example")

scoreboard = Scoreboard()
scoreboard.show_score()

# Simulate increasing the score
scoreboard.increase_score()

# Keep the window open
screen.mainloop()
