from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen() 
# score = 0

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# Tracer turns of the automatic update/animation on the screen and screen needs to be updated manually.


# Create the snake body 
snake  = Snake()
# Create food
food = Food()
# Create the scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food 
    # Using the distance method from the turtle library.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # scoreboard.clear()
        # This is clear the previous scoreboard 
        # This can be called in the scoreboard class as well.
        scoreboard.increase_score()
    
    # Detect collioson with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect Collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

