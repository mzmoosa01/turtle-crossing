from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-280, 250)
        self.level = 0
        self.write_level()

    def level_up(self):
        self.level += 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.level = 0
        self.write('Game Over', font=FONT)

    def reset_game(self):
        self.setpos(-280, 250)
        self.level = 0
        self.write_level()
