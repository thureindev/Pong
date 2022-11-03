from turtle import Turtle
import random
import game_settings as gs


class GameUI(Turtle):
    def __init__(self):
        super().__init__()
        self.playground = Turtle()
        self.setup_playground()

        self.score_ui = Turtle()
        self.setup_score_ui()

    def setup_playground(self):
        self.playground.hideturtle()
        self.playground.pencolor(gs.WALL_COLOR)

        self.draw_boundaries()

    def setup_score_ui(self):
        self.score_ui.hideturtle()
        self.score_ui.penup()
        self.score_ui.color(gs.FONT_COLOR)

        self.update_scores(0, 0)

    def update_scores(self, p1_score, p2_score):
        self.score_ui.clear()
        self.score_ui.color(gs.FONT_COLOR)

        self.score_ui.goto(-50, gs.HEIGHT_LIMIT - 50)
        self.score_ui.write(f"{p1_score}", align='right', font=gs.FONT)
        self.score_ui.goto(50, gs.HEIGHT_LIMIT - 50)
        self.score_ui.write(f"{p2_score}", align='left', font=gs.FONT)

    def display_scored_player(self, scored_p, status="SCORED!"):
        self.score_ui.goto(0, gs.HEIGHT_LIMIT - 100)
        self.score_ui.color(gs.SCORED_COLOR)
        self.score_ui.write(f"{scored_p.name} {status}", align='center', font=gs.FONT)

    def display_winner(self, winner, status="WINS!"):
        self.score_ui.goto(0, 0)
        self.score_ui.color(gs.WINNER_COLOR)
        self.score_ui.write(f"{winner.name} {status}", align='center', font=gs.FONT)

    def display_game_paused(self, status="PAUSED"):
        self.score_ui.goto(0, 0)
        self.score_ui.color(gs.FONT_COLOR)
        self.score_ui.write(f"{status}", align='center', font=gs.FONT)

    def display_gamestart_key(self, action_word="start game"):
        self.score_ui.goto(0, -gs.HEIGHT_LIMIT + 100)
        self.score_ui.color(gs.FONT_COLOR)
        self.score_ui.write(f"Press spacebar to {action_word}", align='center', font=gs.FONT)

    def draw_boundaries(self):
        self.playground.penup()
        self.playground.setpos(-gs.WIDTH_LIMIT, gs.HEIGHT_LIMIT)
        self.playground.pendown()
        self.playground.pensize(5)
        # draw 4 walls
        self.playground.goto(gs.WIDTH_LIMIT, gs.HEIGHT_LIMIT)
        self.playground.goto(gs.WIDTH_LIMIT, -gs.HEIGHT_LIMIT)
        self.playground.goto(-gs.WIDTH_LIMIT, -gs.HEIGHT_LIMIT)
        self.playground.goto(-gs.WIDTH_LIMIT, gs.HEIGHT_LIMIT)
        # draw score line
        self.playground.goto(0, gs.HEIGHT_LIMIT)
        self.playground.goto(0, gs.HEIGHT_LIMIT - 60)

