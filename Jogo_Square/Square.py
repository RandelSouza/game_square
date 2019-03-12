# -*- coding:UTF-8 -*-

class Square(object):
    def __init__(self, position, image, speed=1, cor=None):
        print position
        self.image = image
        self.position = list(position[:])
        self.speed = speed
        self.cor = cor
