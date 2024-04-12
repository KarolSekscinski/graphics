from camera import *
from projection import *
from object_3d import *


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.rotate_y(math.pi / 6)
        self.object.translate([0.2, 0.2, 0.2])

    def draw(self):
        self.screen.fill(pg.Color('black'))
        self.object.draw()

    def run(self):
        while True:
            # drawing background and objects
            self.draw()
            # camera controls and events
            self.camera.control()
            # scan for exit
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()
