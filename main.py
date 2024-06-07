from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# tracer(0) method of screen restricts display untill screen.update() is called
# here argument is the number of turtle actions before screen is updated

snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey( fun = snake.up, key = "Up")
screen.onkey( fun = snake.down, key = "Down")
screen.onkey( fun = snake.right, key = "Right")
screen.onkey( fun = snake.left, key = "Left")

game_is_on = True
while game_is_on:
    screen.update()
    # all the codes below this inside while loop are executed then only execution is shown
    # in the screen since we are using tracer and update() methods. What this does is
    # doesnot shows the separation of turtle objects. This is useful if we want parallel
    # execution of lines of code in pop.
    # This method renders all the turtle actions that have occurred since the last update.
    # It is especially useful when you need to perform multiple drawing actions quickly
    # without updating the screen each time.
    time.sleep(0.15)
    # it means delay time by 0.5 seconds and update the screen
    # The time.sleep() function from the time module is used to pause the execution of
    # the program for a specified number of seconds. It can be useful to control the timing
    # of the animation, making the turtle wait for a certain period before executing the next action.
    snake.move()


    # detect collision with food
    if snake.head.distance(food) < 15:
        # distance method in turtle class measures distance between the self object
        # and object that is passed as argument
        food.refresh()
        scoreboard.update_score()
        scoreboard.show_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision with itself
    for segment in snake.segments[1:]:
        # using slicing here to skip fist segment i.e head as there is always collision of head and head
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
