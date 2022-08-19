from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        new_car = Turtle()
        car_y = randint(-240, 240)
        color = choice(COLORS)

        new_car.shape('square')
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.setpos(310, car_y)
        new_car.color(color)

        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.fd(self.move_distance)

    def check_collision(self, player: Turtle):
        for car in self.cars:
            x_distance = player.xcor() - car.xcor()
            y_distance = player.ycor() - car.ycor()
            if abs(x_distance) <= 30 and abs(y_distance) <= 30:
                return True

        return False

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

    def reset(self):
        for car in self.cars:
            car.reset()
            car.hideturtle()

        self.cars = []
        self.create_car()
        self.move_distance = STARTING_MOVE_DISTANCE
