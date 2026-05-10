from turtle import Turtle
import random

class Food(Turtle): # Inherit from Turtle superclass
    def __init__(self):
        super().__init__() # calling the Turtle's superclass, superclass call
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # normally 20x20 pixels, but we're halving it to 10x10
        self.color("green")
        self.speed("fastest") # food creation
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
