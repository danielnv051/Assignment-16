import random
from typing import Optional
import arcade
from arcade import Texture


# class Ball
class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.YELLOW
        self.radius = 15
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.speed = 3

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)


# class Rocket
class Rocket(arcade.Sprite):
    def __init__(self, x, y, color, n):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = color
        self.name = n
        self.change_x = 0
        self.change_y = 0
        self.width = 10
        self.height = 60
        self.speed = 4
        self.score = 0

    def move(self):
        ...

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color
        )


# class Game
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Pong 2023🏓", center_window=True)
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.player_1 = Rocket(40, self.height // 2, arcade.color.RED, "Daniel")
        self.player_2 = Rocket(
            self.width - 40, self.height // 2, arcade.color.BLUE, "Computer"
        )
        self.ball = Ball(self)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_outline(
            self.width // 2,
            self.height // 2,
            self.width - 30,
            self.height - 30,
            arcade.color.WHITE,
            border_width=10,
        )

        arcade.draw_line(
            self.width // 2,
            30,
            self.width // 2,
            self.height - 30,
            arcade.color.WHITE,
            line_width=10,
        )

        arcade.draw_text(
            self.player_1.name, self.width // 5, 40, arcade.color.WHITE, font_size=20
        )
        arcade.draw_text(
            self.player_2.name,
            self.width - self.width // 3,
            40,
            arcade.color.WHITE,
            font_size=20,
        )
        arcade.draw_text(
            self.player_1.score,
            self.width // 4,
            self.height - 60,
            arcade.color.WHITE,
            font_size=25,
        )
        arcade.draw_text(
            self.player_1.score,
            self.width - self.width // 4,
            self.height - 60,
            arcade.color.WHITE,
            font_size=25,
        )

        self.player_1.draw()
        self.player_2.draw()
        self.ball.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player_1.height < y < self.height - self.player_1.height:
            self.player_1.center_y = y

    def on_update(self, delta_time: float):
        self.ball.move()


game = Game()
arcade.run()
