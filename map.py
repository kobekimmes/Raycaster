import pygame as pg


_ = False
map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1]
    ]

class Map:

    def __init__(self, game):
        self.game = game
        self.map = map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j]:
                    self.world_map[(i, j)] = 1



    def draw(self):
        [pg.draw.rect(self.game.screen, "darkgray", (x*self.game.res, y*self.game.res, self.game.res, self.game.res),2)
        for (x,y) in self.world_map]



