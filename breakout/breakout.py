import random
import arcade


class Ball(arcade.Sprite):
    ...


class Stone(arcade.Sprite):
    ...


class Rocket(arcade.Sprite):
    ...


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="BreakOut", center_window=True)
        self.background = arcade.load_texture(
            ":resources:images/backgrounds/abstract_1.jpg"
        )
        self.width = 800
        self.height = 600
        

    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.width, self.height, self.background
        )

        arcade.finish_render()


game = Game()
arcade.run()
