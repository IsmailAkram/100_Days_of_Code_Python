from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
STARTING_POS = (-220, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(STARTING_POS)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"LEVEL: {self.level}", align=ALIGNMENT, font=FONT)

    def tally(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over_status(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

