import pygame, sys
from model import Model
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
screenColor = (0, 0, 0)

class Controller:
    def __init__(self, v):
        self.view = v


    def startGame(self):
        p1 = Model()
        p1.makeRect(20, 90, 10, 150)
        while True:
            for event in self.view.getEvents():
                if event.type == pygame.QUIT:
                    self.view.endGame()
                    sys.exit()
            self.view.backgroundFill(screenColor)
            

    def moveRect(self, rect):
        rectSpeed = 5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.shape.x > 0:
            self.shape.move_ip(-rectSpeed,0)
        elif keys[pygame.K_RIGHT] and self.shape.x < SCREEN_WIDTH - self.shape.width:
            self.shape.move_ip(rectSpeed,0)
        elif keys[pygame.K_DOWN] and self.shape.y < (SCREEN_HEIGHT - self.shape.height):
            self.shape.move_ip(0, rectSpeed)
        elif keys[pygame.K_UP] and self.shape.y > 0:
            self.shape.move_ip(0, -rectSpeed)   
