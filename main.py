"""PONG game"""
from turtle import Screen
import time
import game_settings as gs
from ball import Ball, is_right_dir as ball_dir_right, is_left_dir as ball_dir_left
from gameui import GameUI
from player import Player
from game import Game


def main():
    gui = GameUI()

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

    screen.update()

    game = Game()

    def game_start():
        game.is_gameover = False
        match_winning_score = 3

        player_1.reset_score()
        player_2.reset_score()

        gui.update_scores(0, 0)
        ball.reset_pos()

        while not game.is_gameover:
            if not game.is_paused:
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
                            gui.update_scores(player_1.score, player_2.score)
                            gui.display_scored_player(player_2)
                            screen.update()
                            if player_2.score >= match_winning_score:
                                gui.display_winner(player_2)
                                game.gameover()
                                gui.display_gamestart_key(action_word="restart game")
                                screen.update()
                            else:
                                ball.reset_pos()
                            time.sleep(1)

                elif ball_dir_right(ball.heading()):
                    # check collision player paddles
                    if not ball.is_collided_with_paddle(player_2.paddle):

                        # check if paddle missed and other player scored
                        if ball.hit_score_line(player_1.score_line_xcor):
                            player_1.add_score()
                            gui.update_scores(player_1.score, player_2.score)
                            gui.display_scored_player(player_1)
                            screen.update()
                            if player_1.score >= match_winning_score:
                                gui.display_winner(player_1)
                                game.gameover()
                                gui.display_gamestart_key(action_word="restart game")
                                screen.update()
                            else:
                                ball.reset_pos()
                            time.sleep(1)

                time.sleep(gs.CLOCK_TICK)

            # else:
            #     gui.display_game_paused()
            #     gui.display_gamestart_key(action_word="to continue")

            screen.update()

    # to start a new game
    game.gameover()
    gui.display_gamestart_key()

    def check_pause_and_game_restart():
        print(f"gameover: {game.is_gameover}")
        print(f"paused: {game.is_paused}")
        if game.is_gameover:
            game_start()
        else:
            game.toggle_pause()

    screen.onkeypress(key="space", fun=check_pause_and_game_restart)
    # while True:
    #     game_start()


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

