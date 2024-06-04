
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.show_score()


    def update_score(self):
        self.score += 1

    def show_score(self):
        self.clear()
        # clears the previous turtle drawing
        self.goto(x= 0, y= 270)
        # moves to the same position
        self.write(arg = f"Score: {self.score}", move = True, align = ALIGNMENT, font= FONT)
        # writes the score again

    def game_over(self):
        self.goto(0,0)
        self.write(arg = f" GAME OVER ", move = True, align = ALIGNMENT, font= FONT)

