from turtle import Turtle, Screen

tim  = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_left():
    time_head = tim.heading()+10
    tim.setheading(time_head)
    
def turn_right():
    time_head = tim.heading()-10
    tim.setheading(time_head)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(key = 'w',fun = move_forwards)
screen.onkey(key = 's',fun = move_backwards)
screen.onkey(key = 'a',fun = turn_left)
screen.onkey(key = 'd',fun = turn_right)
screen.onkey(key = 'c',fun = clear)
screen.exitonclick()