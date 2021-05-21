from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.y_bounce()


    if ball.distance(r_paddle) < 60 and ball.xcor() >340 or ball.distance(l_paddle) < 60 and ball.xcor() < -340:
        ball.x_bounce()


    if ball.xcor() > 380 :
        ball.reset_position()
        score.l_point() 
        game_is_on = score.check()   

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        game_is_on = score.check()

screen.exitonclick()    