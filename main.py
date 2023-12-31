import pygame as pg
import sys
from map import *
from camera import *
from raycasting import *

class Game:

    WIDTH, HEIGHT = 1600, 800

    def __init__(self, res, FPS):
        pg.init()

        self.WIDTH = res * 40
        self.HEIGHT = res * 20
        self.running = True
        self.res = res
        self.FPS = FPS
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.newGame()

    def newGame(self):
        self.map = Map(self)
        self.camera = Camera(self, self.WIDTH//4, self.HEIGHT//2)
        self.ray = Raycast(self)

    def update(self):
        self.camera.update()
        self.ray.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(self.FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def show2DGrid(self):
        for i in range(self.res):
            pg.draw.aaline(self.screen, "white", (i * self.res, 0), (i * self.res, self.HEIGHT), )
        for j in range(self.res):
            pg.draw.aaline(self.screen, "white", (0, j * self.res), (self.WIDTH//2, j * self.res), )

    def draw(self):
        self.screen.fill("black")
        #self.show2DGrid()
        self.map.draw()
        self.camera.draw()

    def run(self):
        while self.running:
            self.draw()
            self.update()
            self.checkEvents()
        pg.quit()


if __name__ == "__main__":
    game = Game(30, 60)
    game.run()
