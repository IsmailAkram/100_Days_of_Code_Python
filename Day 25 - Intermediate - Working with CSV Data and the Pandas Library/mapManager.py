from turtle import Turtle, Screen

FONT = ("Courier", 24, "bold")

class MapManager(Turtle):
    def __init__(self, screen_title, image, data_file, total_count):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.total = total_count

        # Initializing Screen
        self.screen = Screen()
        self.screen.title(screen_title)
        self.screen.addshape(image)

        self.bg = Turtle()
        self.bg.shape(image)

    def map_state(self, state, x, y):
        self.goto(x, y)
        self.write(state)
        self.score += 1

    def show_final_score(self):
        self.goto(0,0)
        self.write(f"GAME OVER\nFinal Score: {self.score}/{self.total}", align="center", font=FONT)
        self.screen.exitonclick()