# -*- coding:UTF-8 -*-

import pygame, random
import funcoes
import setup

background, backgroundRect, screen, q, jogador1, jogador2 = funcoes.iniciar()
a = True

while setup.RUNNING:
    funcoes.exit_game()

    while a:
        tecla_pressionada = pygame.key.get_pressed()
        funcoes.exit_game()
        setup.clock.tick(60)
        screen.blit(background, backgroundRect)
        funcoes.desenhar_t1_t2_tm(screen)
        funcoes.time_jogo()
        q = funcoes.atualizarQuadrados(q)
        player1, player2 = funcoes.movimentar_desenhar_jogadores(screen, tecla_pressionada, jogador1, jogador2)
        funcoes.quadrado_collissao(q, screen, player1, player2)
        pygame.display.update()
