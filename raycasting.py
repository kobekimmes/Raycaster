import pygame as pg
import math


class Raycast:

    def __init__(self, game):
        self.game = game
        self.FOV = math.pi / 4

        self.num_rays = self.game.res * 10
        self.max_depth = 20
        self.delta_angle =  self.FOV / self.num_rays

    def showRays(self):
        cam_x, cam_y = self.game.camera.get_pos
        map_x, map_y = self.game.camera.get_map_pos
        # print(self.FOV, self.delta_angle)
        # print(cam_x, cam_y)
        # print(map_x,map_y)

        ray_angle = self.game.camera.angle - (self.FOV / 2) + 0.0001
        for ray in range(self.num_rays):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            inc = self.game.res

            #horizontal checks
            y_hor, dy = (map_y + 1, 1) if sin_a > 0 else (map_y - 1e-6, -1)
            depth_hor = (y_hor - cam_y) / sin_a
            x_hor = (cam_x + depth_hor) * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(self.max_depth):
                tile_hor = (int(x_hor), int(y_hor))
                print("tile hor: ", tile_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            #vertical checks
            x_vert, dx = (map_x + 1, 1) if cos_a > 0 else (map_x - 1e-6, -1)
            depth_vert = (x_vert - cam_x) / cos_a
            y_vert = (cam_y + depth_vert) * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(self.max_depth):
                tile_vert = (int(x_vert), int(y_vert))
                print("tile vert: ", tile_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            depth = depth_vert if depth_vert < depth_hor else depth_hor

            pg.draw.line(self.game.screen, (255, 255, 0, 0.25), (cam_x * inc, cam_y * inc),
                         (cam_x * depth * cos_a * inc, cam_y * depth * sin_a * inc), 2)

            ray_angle += self.delta_angle

    def update(self):
        self.showRays()