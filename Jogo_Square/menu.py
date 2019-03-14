from setup import *
import pygame, sys, os
from pygame.locals import *

class Menu( object ):
     def __init__( self ):
         self.init = pygame.init()
         self.screen = pygame.display.set_mode( [ LARGURA, ALTURA ] )
