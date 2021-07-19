from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


def input(key):
    global bullets
    if key == "left mouse down":
        bullet = Bullet()
        bullets.append(bullet)


class Player(FirstPersonController):
    def __init__(self, position=(0, 5, 0)):
        super().__init__(
            position=position,
            mouse_sensitivity=Vec2(50, 40),
            speed=20,
        )


class Sky(Entity):
    def __init__(self):
        super().__init__(
            model="sphere",
            color=color.hex("#99ebff"),
            double_sided=True,
            scale=(100, 100, 100)
        )


class Floor(Entity):
    def __init__(self):
        super().__init__(
            position=(0, 0, 0),
            model="cube",
            scale=(16, 1, 16),
            collider="box",
            color=color.hex("#29e370")
        )


class Bullet(Entity):
    def __init__(self):
        super().__init__(
            position=player.position,
            model="sphere",
            collider="sphere",
            scale=(.05, .05, .5),
            rotation=player.rotation,
        )

    # TODO add bullet movement
    # def update(self):
        # self.position += Vec3(0, 0, 1) * time.dt


class Target(Entity):
    def __init__(self, position=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(
            position=position,
            model="sphere",
            scale=scale,
            collider="sphere",
            color=color.rgb(random.randint(215, 255), 88, 66, random.randint(225, 255)),
        )


bullets = []
sky = Sky()
floor = Floor()
player = Player()
for i in range(5):
    target = Target(position=(i*2-4, 2, 7), scale=(1.5, 4, 1.5))

app.run()
