# import colorgram
#
# rbg_colours = []
# colours = colorgram.extract("image.jpeg", 100)
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#
#     new_colour = (r, g, b)
#     rbg_colours.append(new_colour)
#
# print(rbg_colours)
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
colour_list = [(234, 225, 84), (195, 8, 69), (231, 54, 132), (197, 77, 17), (113, 177, 213), (194, 164, 14), (216, 162, 102), (29, 104, 167), (34, 187, 113), (14, 24, 64), (20, 29, 169), (231, 224, 7), (215, 134, 177), (201, 32, 132), (14, 182, 210), (231, 167, 197), (127, 188, 161), (10, 48, 28), (54, 20, 10), (40, 132, 75), (140, 218, 203), (108, 92, 210), (235, 64, 34), (131, 217, 231), (183, 17, 8), (11, 96, 53), (75, 10, 28), (167, 182, 234), (242, 167, 153), (10, 84, 102), (253, 4, 50), (64, 95, 11), (248, 12, 8), (15, 46, 248)]

#starting position
michelangelo = Turtle()

michelangelo.penup()
michelangelo.hideturtle()
michelangelo.setheading(225)
michelangelo.forward(300)
michelangelo.setheading(0)

michelangelo.speed("fastest")

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    michelangelo.dot(20, random.choice(colour_list))
    michelangelo.forward(50)

    if dot_count % 10 == 0:
        michelangelo.setheading(90)
        michelangelo.forward(50)
        michelangelo.setheading(180)
        michelangelo.forward(500)
        michelangelo.setheading(0)

screen = Screen()
screen.exitonclick()
