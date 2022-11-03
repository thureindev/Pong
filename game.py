from turtle import Turtle


class Game:
    def __init__(self):
        self.is_gameover = False
        self.is_paused = False

    def reset_game(self):
        self.is_gameover = False

    def gameover(self):
        self.is_gameover = True

    def toggle_pause(self):
        if self.is_paused:
            self.is_paused = False
        else:
            self.is_paused = True

        return self.is_paused
