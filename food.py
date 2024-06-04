from turtle import Turtle
import random

class Food(Turtle):
    # now food object is also the turtle object as we have inherited turtle class in food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        #shape of food turtle
        self.color("blue")
        # color of food turtle
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        # size of food turtle is made half of default turtle's size
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

