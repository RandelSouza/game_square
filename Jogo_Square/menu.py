from setup import *
import pygame, sys, os
from pygame.locals import *

class Menu( object ):
    def __init__( self ):
         self.init = pygame.init()
         self.screen = pygame.display.set_mode( [ LARGURA, ALTURA ] )
         self.background = None # pygame.image.load( "image/menu1.png" ).convert()
         self.fps = pygame.time.Clock().tick( 60 )
         self.play =  None #pygame.transform.scale( pygame.image.load( "image/play.png" ).convert(), ( 150, 100 ) )
         pygame.font.init()kkk

    def drawAndUpdateMenu( self ):
        self.screen.blit( self.background, ( 0, 0 ) )
        self.screen.blit( self.play, [ 300, 300 ] )
        pygame.display.update()
