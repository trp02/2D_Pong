import pygame, sys

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600

class Model:
    def __init__(self):
        self.shape = 0 
        self.x = 0
        self.y = 0
        self.rad = 0
        
    def makeRect(self, rectX, rectY, rectW, rectH):
        self.shape = pygame.Rect(rectX, rectY, rectW, rectH)
        
    def makeCircle(self, circX, circY, circRad):
        self.x = circX
        self.y = circY
        self.rad = circRad
        self.shape = pygame.Rect(circX, circY, circRad, circRad)

    def setCords(self, xVelocity, yVelocity):
        self.x = self.x + xVelocity
        self.y = self.y + yVelocity
        self.shape = pygame.Rect(self.x, self.y, self.rad, self.rad)
        
    def getCords(self):
        return (self.x, self.y, self.rad)
    

    def getObj(self):
        return self.shape
    
            