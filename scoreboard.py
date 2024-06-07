
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

file = open(file="data.txt",mode= "r")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = file.read()
        file.close()
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
        self.write(arg = f"Score: {self.score} Highscore: {self.highscore}", move = True, align = ALIGNMENT, font= FONT)
        # writes the score again

    def reset(self):

        if self.score > int(self.highscore):
            file = open("data.txt", mode="w")
            self.highscore = self.score
            file.write(f"{self.score}")
            file.close()
        self.score = 0
        self.show_score()
