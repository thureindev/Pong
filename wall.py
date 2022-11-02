from turtle import Turtle
import random
import game_settings as gs


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

        self.pensize(5)
        self.pencolor(gs.WALL_COLOR)
        self.penup()

    def draw_boundaries(self):
        self.penup()
        self.setpos(-gs.WIDTH_LIMIT, gs.HEIGHT_LIMIT)
        self.pendown()
        self.goto(gs.WIDTH_LIMIT, gs.HEIGHT_LIMIT)
        self.goto(gs.WIDTH_LIMIT, -gs.HEIGHT_LIMIT)
        self.goto(-gs.WIDTH_LIMIT, -gs.HEIGHT_LIMIT)
        self.goto(-gs.WIDTH_LIMIT, gs.HEIGHT_LIMIT)

