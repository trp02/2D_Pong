import pygame, sys
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
 
class View:

    #initializes board
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("pong")
        self.surface = pygame.display.set_mode(SCREEN_SIZE)
        
    #mostly just drawing functions
    #
    def backgroundFill(self, color):
        self.surface.fill(color)

    def drawRect(self, color, rect):
        pygame.draw.rect(self.surface, color, rect)
        
    def drawCirc(self, color, cords):
        pygame.draw.circle(self.surface, color, (cords[0], cords[1]), cords[2])
        
    #send events to controller
    def getEvents(self):
        return pygame.event.get()
    #button pressed to controller
    def getPressed(self):
        return pygame.key.get_pressed()
    
    def update (self):
        pygame.display.update()
        
    def endGame(self):
        pygame.quit
    
    