import pygame
TIME = 0
count = 0
count4 = 0
SCORE1 = 0
SCORE2 = 0
ALTURA = 600
LARGURA = 800

pygame.font.init()
clock = pygame.time.Clock()
fuente = pygame.font.Font(None, 50)

VERDE = pygame.image.load("Imagens/dngn_green_crystal_wall.png")
VERMELHO = pygame.image.load("Imagens/dngn_red_crystal_wall.png")
CORES = [VERDE, VERMELHO]
RUNNING = True
RUNNING2 = True
