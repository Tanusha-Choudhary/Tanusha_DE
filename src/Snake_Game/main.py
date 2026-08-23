import time
from snake import Snake
from Food import Food
from score_board import ScoreBoard
from turtle import Screen,Turtle
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)
snake = Snake()
food = Food()
SB = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# move()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#     Detection of collision
    if snake.head.distance(food) < 15:
        food.refresh()
        SB.increase_score()
        snake.extend_body()
    #     Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        SB.reset_score()
        snake.reset_snake()
#     Detect tail collision
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) < 7:
            SB.reset_score()
            # SB.game_over()
            snake.reset_snake()

screen.exitonclick()
