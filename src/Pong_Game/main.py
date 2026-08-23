from turtle import Screen,Turtle
from paddle import Paddle
import time
from ball import Ball
from Score_Board import Score_B
def main():
    is_game_on = True
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Pong")
    screen.tracer(0) # to move everything fast
    paddle_l = Paddle((-350,0))
    paddle_r = Paddle((350,0))
    # paddle_m = Paddle((50,0))
    ball = Ball()
    screen.listen()
    score = Score_B()
    screen.onkey(paddle_l.up_paddle, "w")
    screen.onkey(paddle_l.down_paddle, "s")
    screen.onkey(paddle_r.up_paddle, "Up")
    screen.onkey(paddle_r.down_paddle, "Down")
    # screen.onkey(paddle_2.up_paddle, "Up")
    # screen.onkey(paddle_2.down_paddle, "Down")
    while is_game_on:
        # paddle_5.
        # time.sleep(0.1)
        ball.ball_move()
        screen.update()
        time.sleep(ball.move_speed)
        # Detect the collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
    #     Detect the collision with paddle
        if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
            # print("Made contact")
            ball.bounce_x()
        if ball.xcor() >  380:
            ball.reset_position()
            score.l_point()
            screen.update()
        if ball.xcor() < -380:
            ball.reset_position()
            score.r_point()
            screen.update()

    screen.exitonclick()
if __name__ == "__main__":
    main()
