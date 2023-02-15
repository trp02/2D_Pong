import pygame, sys
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500

class View:


    def __init__(self, m):
        self.model = m
        pygame.init()
        pygame.display.set_caption("pong")
        self.surface = pygame.display.set_mode(SCREEN_SIZE)
        
    def getEvents(self):
        return pygame.event.get()

    def backgroundFill(self, color):
        self.surface.fill(color)

    
    def endGame(self):
        pygame.quit
    
    