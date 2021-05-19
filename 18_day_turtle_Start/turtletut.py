from turtle import Turtle, Screen, colormode
"""
timmy_the_turtle = Turtle()

timmy_the_turtle.shape('turtle')

timmy_the_turtle.color('red')

for i in range(4):
    timmy_the_turtle.forward(100)

    timmy_the_turtle.right(90)



tim = Turtle()
tim.color('green')
tim.left(90)
tim.penup()
tim.forward(100)
tim.pendown()
for _ in range(5):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


"""
"""
def shape(leng,color):
    ang= 360/leng
    ti.color(color)
    
    for _ in range(leng):
        
        ti.forward(100)
        ti.right(ang)
        


ti = Turtle()
ti.color('green')

shape(3,'blue')
shape(4,'black')
shape(5,'red')
shape(6,'yellow')
shape(7,'pink')
shape(8,'orange')


"""
"""
tim = Turtle()
colormode(255)
########### Challenge 4 - Random Walk ########
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

"""


import random

til = Turtle()
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

til.speed('fastest')
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        til.color(random_color())
        til.circle(100)
        current_heading = til.heading()
        til.setheading(current_heading + size_of_gap)


draw_spirograph(5)



screen = Screen()
screen.exitonclick()