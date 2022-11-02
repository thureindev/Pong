from turtle import Turtle
import random
import game_settings as gs


def dir_choice():
    max_angle = random.randint(gs.BALL_MIN_ANGLE, gs.BALL_MAX_ANGLE)
    return random.choice([max_angle, max_angle + 90, max_angle + 180, max_angle + 270])


def is_right_dir(heading):
    if heading < 90 or heading > 270:
        return True
    return False


def is_left_dir(heading):
    if 90 < heading < 270:
        return True
    return False


def is_bounce_dead_horz_dir(heading):
    if heading == 0 or heading == 180:
        return True
    return False


def is_bounce_dead_vert_dir(heading):
    if heading == 90 or heading == 270:
        return True
    return False


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color(gs.BALL_COLOR)
        self.speed = gs.BALL_SPEED

        self.reset_pos()

    def reset_pos(self):
        self.setpos(0, random.randint(-gs.HEIGHT_LIMIT + 50, gs.HEIGHT_LIMIT - 50))
        self.setheading(dir_choice())

    def move(self):
        self.forward(self.speed)

    def is_collided_with_wall_boundary(self):
        top_wall = gs.HEIGHT_LIMIT
        bot_wall = -gs.HEIGHT_LIMIT

        # hit TOP_WALL                               OR hit BOT_WALL
        if self.y_distance(top_wall) <= gs.BLOCK_SIZE or self.y_distance(bot_wall) <= gs.BLOCK_SIZE:
            self.bounce_on_y()
            return True

        return False

    def is_collided_with_paddle(self, paddle):
        # if paddle.xcor() > 0:
        #     if self.xcor() + gs.BLOCK_SIZE < paddle.xcor():
        #         return False
        # else:
        #     if self.xcor() - gs.BLOCK_SIZE > paddle.xcor():
        #         return False

        if self.x_distance(paddle.xcor()) <= gs.BLOCK_SIZE:
            if self.y_distance(paddle.ycor()) <= gs.PADDLE_HALF_HEIGHT:
                self.bounce_on_x()
                return True

        return False

    def hit_score_line(self, score_line):
        # if score_line > 0:
        #     if self.xcor() > score_line:
        #         return True
        # else:
        #     if self.xcor() < score_line:
        #         return True

        if self.x_distance(score_line) <= gs.BLOCK_SIZE:
            return True

        return False

    def bounce_on_y(self):
        # I don't know how to explain. Try to understand coordinate graph and vector angles
        angle = 180 + (180 - self.heading())
        if angle > 360:
            angle %= 360
        self.setheading(angle)

    def bounce_on_x(self):
        # I don't know how to explain. Try to understand coordinate graph and vector angles
        self.setheading(180 - self.heading())

    def x_distance(self, other):
        distance = self.xcor() - other
        return abs(distance)

    def y_distance(self, other):
        distance = self.ycor() - other
        return abs(distance)
