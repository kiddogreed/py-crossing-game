import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Crossing Game ")
screen.tracer(0)

screen.listen()
player = Player()
score_board = Scoreboard()
car_manager = CarManager()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detech collision
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            score_board.game_over()
            game_is_on = False

    #detech success
    if player.finished():
        player.goto_start()
        car_manager.level_up()
        score_board.scoring()


screen.exitonclick()



