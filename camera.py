import math
import pygame as pg


class Camera:

    def __init__(self, game, x, y):
        self.game = game
        self.vel = 0.5
        self.rot_speed = 0.001
        self.x = x
        self.y = y
        self.angle = 360

    def move(self):

        self.sin_a = math.sin((self.angle))
        self.cos_a = math.cos((self.angle))

        dx, dy = 0, 0
        speed_x = (self.vel * self.sin_a) * self.game.delta_time
        speed_y = (self.vel * self.cos_a) * self.game.delta_time

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            dx += speed_x
            dy += speed_y

        if keys[pg.K_s]:
            dx -= speed_x
            dy -= speed_y

        if keys[pg.K_d]:
            dx -= speed_y
            dy += speed_x

        if keys[pg.K_a]:
            dx += speed_y
            dy -= speed_x

        self.check_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle += self.rot_speed * self.game.delta_time

        if keys[pg.K_RIGHT]:
            self.angle -= self.rot_speed * self.game.delta_time

        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x//self.game.res,y//self.game.res) not in self.game.map.world_map

    def check_collision(self, dx ,dy):
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx

    def draw(self):
        pg.draw.line(self.game.screen, (255,255,255), (self.x, self.y),
                     (self.x + (self.game.res) * math.sin(self.angle),
                      self.y + (self.game.res) * math.cos(self.angle)), 2)
        pg.draw.circle(self.game.screen, (255, 0, 0), (self.x, self.y), self.game.res//4)


    def update(self):
        self.move()

    @property
    def get_pos(self):
        return self.x / self.game.res, self.y / self.game.res

    @property
    def get_map_pos(self):
        return self.x // self.game.res, self.y // self.game.res

    @property
    def get_real_pos(self):
        return self.x, self.y


