from ursina import *

app = Ursina()




# player = Entity(model='cube', color=color.orange, scale = (0.3, 2), position = (-6, 0, 0))
# player2 = Entity(model='cube', color=color.green, scale = (0.3, 2), position = (6, 0, 0))
#
# def update():   # update gets automatically called.
#     player.y += held_keys['w'] * .06
#     player.y -= held_keys['s'] * .06
#     player2.y += held_keys['up arrow'] * .06
#     player2.y -= held_keys['down arrow'] * .06
#
#



'''example of inheriting Entity'''
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model='cube'
        self.color = color.red
        self.scale_y = 2
        self.scale = (0.3, 2)
        self.position = (-6, 0, 0)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'space':
            for loop in range(0, 500):
                self.animate_z(loop, duration=1)
        if key == 'x':
            self.animate_origin_x()
        # if key == 'z':
        #     self.animate_x(-6, duration=1)

    def update(self):
        self.y += held_keys['w'] * time.dt * 10
        self.y -= held_keys['s'] * time.dt * 10

player = Player(x=-6, color = color.red)
# player2 = Player(x=6, color = color.green, player2 = True)


app.run()   # opens a window and starts the game.
