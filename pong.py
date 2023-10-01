import arcade


class Ball(arcade.Sprite):
    ...


class Rocket(arcade.Sprite):
    ...


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Pong 2023🏓", center_window=True)
        arcade.set_background_color(arcade.color.DARK_GREEN)

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
        arcade.finish_render()


game = Game()
arcade.run()
