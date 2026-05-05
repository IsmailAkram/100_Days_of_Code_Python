import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Turtle")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.move_up, "Up")

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.drive()

    # Detect turtle collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over_status()

    # Detect successful crossing
    if player.is_at_finish_line(): # finishing line Y
        scoreboard.tally()
        player.go_to_start()
        car_manager.accelerate()

screen.exitonclick()