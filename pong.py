import arcade

class Ball(arcade.Sprite):
    ...

class Rocket(arcade.Sprite):
    ...

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=700, title="Pong 2023🏓")
        arcade.set_background_color(arcade.color.DARK_GREEN)

    def on_draw(self):
        arcade.start_render()

        arcade.finish_render()

game = Game()
arcade.run()