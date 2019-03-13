# -*- coding:UTF-8 -*-

import pygame, random
import funcoes
import setup
background, backgroundRect, screen, listSquare, jogador1, jogador2 = funcoes.iniciar()

while setup.RUNNING:
    funcoes.exit_game()

    while setup.RUNNING2:
        tecla_pressionada = pygame.key.get_pressed()
        funcoes.exit_game()
        setup.clock.tick(60)
        screen.blit(background, backgroundRect)
        funcoes.desenhar_t1_t2_tm(screen)
        setup.RUNNING2 = funcoes.time_jogo()
        listSquare = funcoes.atualizarQuadrados(listSquare)
        player1, player2 = funcoes.movimentar_desenhar_jogadores(screen, tecla_pressionada, jogador1, jogador2)
        funcoes.quadrado_collissao(listSquare, screen, player1, player2)
        pygame.display.update()
