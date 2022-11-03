from paddle import Paddle
import game_settings as gs


class Player:
    def __init__(self, name="player", is_on_left_side=True):
        self.paddle = Paddle(is_on_left_side)
        self.score = 0
        self.name = name
        if is_on_left_side:
            self.score_line_xcor = gs.WIDTH_LIMIT
        else:
            self.score_line_xcor = -gs.WIDTH_LIMIT

    def add_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0