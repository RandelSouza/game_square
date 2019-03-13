# -*- coding:UTF-8 -*-

class Square(object):
    def __init__(self, position, image, speed=1, cor=None):
        print position
        self.image = image
        self.position = list(position[:])
        self.speed = speed
        self.cor = cor

    def draw_centered(self, surface1, surface2, position):
        rect = surface1.get_rect()
        rect = rect.move(position[0] - rect.width / 2, position[1] - rect.height / 2)
        surface2.blit(surface1, rect)
        return rect

    def draw_on(self, screen):
        rect = self.draw_centered(self.image, screen, self.position)
        return rect

    def movimentar(self, velocidade):
        self.position[1] += velocidade

    def get_cor(self):
        return self.cor

    def set_cor(self, cor):
        self.cor = cor
