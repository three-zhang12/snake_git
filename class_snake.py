import pygame as py
import random


# 头部
class Snake(py.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.image = [py.image.load('images/1.png').convert_alpha(),
                      py.image.load('images/2.png').convert_alpha(),
                      py.image.load('images/3.png').convert_alpha(),
                      py.image.load('images/4.png').convert_alpha(),
                      py.image.load('images/5.png').convert_alpha(),
                      py.image.load('images/6.png').convert_alpha(),
                      py.image.load('images/7.png').convert_alpha(),
                      ]
        self.rect = self.image[0].get_rect()
        self.width, self.height = bg_size
        self.rect.center = (self.width / 2, self.height / 2)
        self.mask = py.mask.from_surface(self.image[0])
        self.active = True

    def move(self, des):
        self.rect = self.rect.move(des)
        if self.rect.bottom < 0:
            self.rect.top = self.height
        if self.rect.top > self.height:
            self.rect.bottom = 0
        if self.rect.right < 0:
            self.rect.left = self.width
        if self.rect.left > self.width:
            self.rect.right = 0


# 身体增加类
class Inc(py.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = [py.image.load('images/1.png').convert_alpha(),
                      py.image.load('images/2.png').convert_alpha(),
                      py.image.load('images/3.png').convert_alpha(),
                      py.image.load('images/4.png').convert_alpha(),
                      py.image.load('images/5.png').convert_alpha(),
                      py.image.load('images/6.png').convert_alpha(),
                      py.image.load('images/7.png').convert_alpha(),
                      ]
        self.rect = self.image[0].get_rect()
        self.rect.center = position
        self.mask = py.mask.from_surface(self.image[0])

    def move(self, des):
        self.rect = self.rect.move(des)


# 果实类
class Enemy(py.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()
        self.image = py.image.load('images/target.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size
        self.rect.left, self.rect.top = random.randint(0, self.width - self.rect.width),\
            random.randint(0, self.height - self.rect.height)
        self.mask = py.mask.from_surface(self.image)

    def reset(self):
        self.rect.left, self.rect.top = random.randint(0, self.width - self.rect.width),\
            random.randint(0, self.height - self.rect.height)


# 障碍类
class Hinder1(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load('images/hinder1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = random.randint(0, 900), random.randint(0, 506)
        self.mask = py.mask.from_surface(self.image)

    def reset(self):
        self.rect.left, self.rect.top = random.randint(0, 900), random.randint(0, 506)


class Hinder2(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load('images/hinder2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = py.mask.from_surface(self.image)


class Hinder3(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load('images/hinder3.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = py.mask.from_surface(self.image)


class Hinder4(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load('images/hinder4.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = py.mask.from_surface(self.image)


class Hinder5(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load('images/hinder5.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = py.mask.from_surface(self.image)