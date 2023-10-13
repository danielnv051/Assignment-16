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
        super().__init__(width=800,height=600,title='BreakOut',center_window=True)
        arcade.load_texture(':resources:images/backgrounds/abstract_1.jpg')

    def on_draw(self):
        arcade.start_render()

        arcade.finish_render()
        

window = Game()
arcade.run()