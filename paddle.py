from turtle import Turtle
import game_settings as gs


class Paddle(Turtle):
    def __init__(self, is_on_left_side=True):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(round(gs.PADDLE_HEIGHT / gs.BLOCK_SIZE), 1, 1)
        self.color(gs.PADDLE_COLOR)
        if is_on_left_side:
            self.setpos(-gs.PADDLE_POS_X, 0)
        else:
            self.setpos(gs.PADDLE_POS_X, 0)
        self.speed = gs.PADDLE_SPEED

    def move_up(self):
        move_distance = self.ycor() + gs.PADDLE_HALF_HEIGHT + gs.PADDLE_SPEED
        # snap movement if upper wall is hit
        if move_distance < gs.HEIGHT_LIMIT:
            self.sety(move_distance)

    def move_down(self):
        move_distance = self.ycor() - gs.PADDLE_HALF_HEIGHT - gs.PADDLE_SPEED
        # snap movement if upper wall is hit
        if move_distance > -gs.HEIGHT_LIMIT:
            self.sety(move_distance)
