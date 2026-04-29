from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

scoreboard = Scoreboard()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # ball.distance(paddle) will only work with center mass,
    # but since paddle is stretched, it will phase through the edges,
    # so we account for boundaries

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        if ball.x_move > 0: # ONLY bounce if moving RIGHT
            ball.reflect()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        if ball.x_move < 0:  # ONLY bounce if moving LEFT
            ball.reflect()

    # When R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.goto(0,0)
        ball.reset_position()

    # When L paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.goto(0,0)
        ball.reset_position()

    if scoreboard.l_score == 5:
        game_is_on = False
        scoreboard.game_over_status_p1_wins()

    if scoreboard.r_score == 5:
        scoreboard.game_over_status_p2_wins()

screen.exitonclick()