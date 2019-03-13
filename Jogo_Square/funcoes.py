import random, pygame, time, setup, pickle, client
from pygame.locals import *
from Square import *
global cliente

cliente = client.Cliente()
random.seed(3)

global player
player = pickle.loads(cliente.recieve_message())

def movimentar_squares1(quadrado1, quadrado2,  tecla_pressionada, velocidade):
    if tecla_pressionada[pygame.K_LEFT]:
        moveLeft(quadrado1, velocidade)
    if tecla_pressionada[pygame.K_RIGHT]:
        moveRight(quadrado1, velocidade)

    limitScreen(quadrado1)

    cliente.send_message(pickle.dumps(quadrado1.position))
    quadrado2.position = pickle.loads(cliente.recieve_message())

def limitScreen(square):
    if square.position[0] == 0:
        square.position[0] += 10
    if square.position[0] == setup.LARGURA:
        square.position[0] -= 10

def moveRight(quadrado, velocidade):
    quadrado.position[0] += velocidade

def moveLeft(quadrado, velocidade):
    quadrado.position[0] -= velocidade

def movimentar_squares2(quadrado1, quadrado2,  tecla_pressionada, velocidade):
    if tecla_pressionada[pygame.K_LEFT]:
        moveLeft(quadrado2, velocidade)
    if tecla_pressionada[pygame.K_RIGHT]:
        moveRight(quadrado2, velocidade)

    limitScreen(quadrado2)

    cliente.send_message(pickle.dumps(quadrado2.position))
    quadrado1.position = pickle.loads(cliente.recieve_message())

def criar_quadrados(quantidade):
    quadrados = []
    for i in range(quantidade):
        cor = random.randint(0,1)
        square = Square([random.randint(0, setup.LARGURA - 90), 0 - (random.randint(1, 700))], setup.CORES[cor])
        square.set_cor(cor)
        quadrados.append(square)
    return quadrados

def desenha_quadrados(quadrado, screen):
    rect = quadrado.draw_on(screen)
    return rect

def colissao_quadrados(quadrado1, quadrado2):
    if quadrado1.colliderect(quadrado2):
        return True
    return False

def criar_jogador(cor):
    jogador = Square([setup.LARGURA / 2, setup.ALTURA - 10], setup.CORES[cor])
    return jogador

def desenhar_jogador(jogador, tela):
    rect = jogador.draw_on(tela)
    return rect

def inicializar_som():
    sound = pygame.mixer.Sound("boom_pack/Coin 3.wav")
    sound.set_volume(0.1)
    sound2 = pygame.mixer.Sound("boom_pack/Hit 5.wav")
    sound2.set_volume(0.1)
    return sound, sound2

def quadrado_collissao(lista_square, screen, player1, player2):
    sound, sound2 = inicializar_som()

    for qua in lista_square:
        quadrado = desenha_quadrados(qua, screen)
        if colissao_quadrados(player1, quadrado):
            if qua.get_cor() == 0:
                sound.play()
                qua.position[1] += 40
                setup.SCORE1 += 1
            else:
                sound2.play()
                qua.position[1] += 40
                setup.SCORE1 -= 1

        if colissao_quadrados(player2, quadrado):
            if qua.get_cor() == 1:
                sound.play()
                qua.position[1] += 40
                setup.SCORE2 += 1
            else:
                sound2.play()
                qua.position[1] += 40
                setup.SCORE2 -= 1

def incrementTime():
    setup.TIME += 1

def transformTimeSeconds():
    if setup.TIME >= 100:
        setup.count4 = setup.TIME / 100
    if setup.TIME == 3000:
        return False
    return True

def time_jogo():
    incrementTime()
    return transformTimeSeconds()

def atualizarQuadrados(quadrados):
    for i in quadrados:
        if i.position[1] == setup.ALTURA + 800:
            quadrados = criar_quadrados(random.randint(1, 60))
        i.position[1] += 1
    return quadrados

def desenhar_t1_t2_tm(screen):
    time = setup.fuente.render(str(setup.count4), 100, (0, 0, 0))
    texto1 = setup.fuente.render("Player1: " + str(setup.SCORE1), 100, (0, 255, 0))
    texto2 = setup.fuente.render("Player2: " + str(setup.SCORE2), 100, (255, 0, 0))
    screen.blit(texto1, (0, 10))
    screen.blit(texto2, (setup.LARGURA - 250, 10))
    screen.blit(time, ((setup.LARGURA / 2) - 50, (setup.ALTURA / 2) - 290))

def movimentar_desenhar_jogadores(screen, tecla_pressionada, jogador1, jogador2):
    if player == -1:
        movimentar_squares1(jogador1, jogador2, tecla_pressionada, 10)

    if player == 1:
        movimentar_squares2(jogador1, jogador2, tecla_pressionada, 10)

    player1 = desenhar_jogador(jogador1, screen)
    player2 = desenhar_jogador(jogador2, screen)
    return player1, player2

def criar_jogadores():
    jogador1 = criar_jogador(0)
    jogador2 = criar_jogador(1)
    return jogador1, jogador2

def exit_game():
    for evento in pygame.event.get():
        if evento.type == QUIT:
            exit()

def iniciar():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("boom_pack/wind.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.2)
    background = pygame.image.load("Imagens/pyramid.jpg")
    backgroundRect = background.get_rect()
    screen = pygame.display.set_mode((setup.LARGURA, setup.ALTURA), 0, 32)
    pygame.display.set_caption('Square')
    listSquare =  criar_quadrados(random.randint(1,60))
    jogador1, jogador2 = criar_jogadores()
    return background, backgroundRect, screen, listSquare, jogador1, jogador2
