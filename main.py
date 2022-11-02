"""PONG game"""
from turtle import Screen
import time
import game_settings as gs
from ball import Ball, is_right_dir as ball_dir_right, is_left_dir as ball_dir_left
from wall import Wall
from player import Player

is_gameover = False


def main():
    wall = Wall()
    wall.draw_boundaries()

    player_1 = Player(name="Player 1", is_on_left_side=True)
    player_2 = Player(name="Player 2", is_on_left_side=False)

    screen.listen()
    # for player 1
    screen.onkeypress(key="w", fun=player_1.paddle.move_up)
    screen.onkeypress(key="s", fun=player_1.paddle.move_down)
    # for player 2
    screen.onkeypress(key="Up", fun=player_2.paddle.move_up)
    screen.onkeypress(key="Down", fun=player_2.paddle.move_down)

    ball = Ball()

    while not is_gameover:
        # update ball movement
        ball.move()

        # check collision with top and bot walls
        ball.is_collided_with_wall_boundary()

        # check paddle bounce or scored point
        if ball_dir_left(ball.heading()):
            # check collision player paddles
            if not ball.is_collided_with_paddle(player_1.paddle):

                # check if paddle missed and other player scored
                if ball.hit_score_line(player_2.score_line_xcor):
                    player_2.add_score()
                    print(f"{player_2.name} score: {player_2.score}")
                    ball.reset_pos()
                    time.sleep(3)

        elif ball_dir_right(ball.heading()):
            # check collision player paddles
            if not ball.is_collided_with_paddle(player_2.paddle):

                # check if paddle missed and other player scored
                if ball.hit_score_line(player_1.score_line_xcor):
                    player_1.add_score()
                    print(f"{player_1.name} score: {player_1.score}")
                    ball.reset_pos()
                    time.sleep(3)

        time.sleep(gs.CLOCK_TICK)
        screen.update()


if __name__ == '__main__':
    screen = Screen()
    screen.tracer(0)
    screen.title("PONG")
    screen.bgcolor("#000000")

    screen.setup(gs.WIDTH_LIMIT * 2, gs.HEIGHT_LIMIT * 2)
    main()
    screen.exitonclick()

#TODO 1.0 CREATE A BALL AND MAKE IT MOVE
#TODO 1.1 DETECT COLLISION WITH OTHER OBJS AND MAKE IT BOUNCE

#TODO 2.0 CREATE PADDLE AND MAKE IT MOVE
#TODO 2.1 MAKE TWO PADDLES FOR BOTH SIDES

#TODO 3.0 CREATE GAMEOBJ    # GAME LOGIC HANDLER
#TODO 4.0 CREATE SCREENOBJ  # GUI HANDLER
#TODO 5.0 CREATE PLAYER    # PLAYER HANDLER
#TODO 6.0 CREATE SCOREBOARD # SCORE HANDLER

