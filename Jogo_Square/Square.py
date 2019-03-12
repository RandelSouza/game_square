# -*- coding:UTF-8 -*-

class Square(object):
    def __init__(self, position, image, speed=1, cor=None):
        print position
        self.image = image
        self.position = list(position[:])
        self.speed = speed
        self.cor = cor

    def draw_on(self, screen):
        rect = draw_centered(self.image, screen, self.position)
        return rect

    # change name method before
    def movimentar(self, velocidade):
        self.position[1] += velocidade

    def get_cor(self):
        return self.cor
