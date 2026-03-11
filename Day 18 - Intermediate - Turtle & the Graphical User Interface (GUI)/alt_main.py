import random
import turtle
from turtle import Turtle, Screen
from random import choice

michelangelo = Turtle()
turtle.colormode(255)
# michelangelo.shape("turtle")
# michelangelo.color("DarkSlateGrey")
michelangelo.hideturtle()
# for _ in range(4):
#     michelangelo.forward(100)
#     michelangelo.right(90)

# for _ in range(4):
#     # michelangelo.forward(100)
#     # michelangelo.right(360/4) # sides
# colours = ["aquamarine4", "DarkSlateGrey", "DeepSkyBlue", "LightCyan4", "lavender", "lightblue3"]

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    rgb_random_colour = (r, g, b)
    return rgb_random_colour

# def draw_shape(sides):
#     for _ in range(sides):
#         michelangelo.forward(100)
#         michelangelo.right(360/sides) # sides
#
# for side in range(3,11):
#     draw_shape(side)
#
#     random_colour = choice(colours) # random.choice
#     michelangelo.color(random_colour)

# # Random Walk
# direction = [0, 1, 2, 3]
# michelangelo.pensize(5)
# michelangelo.speed("fastest")
#
# for _ in range(200):
#     michelangelo.color(random_colour())
#     michelangelo.setheading(90*choice(direction))
#     # michelangelo.right(90*choice_of_direction)
#     michelangelo.forward(10)

# Spirograph
michelangelo.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        michelangelo.color(random_colour())
        michelangelo.circle(150)
        # michelangelo.right(size_of_gap)
        michelangelo.setheading((michelangelo.heading() + size_of_gap))
draw_spirograph(5)

screen = Screen()
screen.exitonclick()
