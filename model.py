import pygame, sys

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500

class Model:
    def __init__(self):
        self.shape = 0 

    def makeRect(self, rectX, rectY, rectW, rectH):
        self.shape = pygame.Rect(rectX, rectY, rectW, rectH)

    
            