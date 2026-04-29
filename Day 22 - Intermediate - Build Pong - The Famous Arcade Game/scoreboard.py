from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over_status_p1_wins(self):
        self.goto(0, 0)
        self.write("GAME OVER: Player 1 Wins!", align=ALIGNMENT, font=FONT)

    def game_over_status_p2_wins(self):
        self.goto(0, 0)
        self.write("GAME OVER: Player 2 Wins!", align=ALIGNMENT, font=FONT)