import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()


def reset_game():
    print('reset')
    player.go_to_start()
    cars.reset()
    scoreboard.reset_game()
    start_game()


def start_game():
    game_is_on = True
    counter = 0
    while game_is_on:
        time.sleep(0.1)
        cars.move_cars()
        counter += 1

        if counter >= 6:
            cars.create_car()
            counter = 0

        # Handle collision with car
        if cars.check_collision(player):
            game_is_on = False
            scoreboard.game_over()

        # handle finish line hit
        if player.ycor() > 280:
            scoreboard.level_up()
            cars.increase_speed()
            player.go_to_start()
        screen.update()


screen.listen()
screen.onkeypress(fun=player.move, key='Up')
screen.onkeypress(fun=reset_game, key='r')

start_game()

screen.exitonclick()

