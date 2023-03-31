import pygame, sys

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600

class Model:
    def __init__(self):
        self.shape = 0 
        self.x = 0
        self.y = 0
        self.rad = 0
    
    #creates a rectangle
    def makeRect(self, rectX, rectY, rectW, rectH):
        self.shape = pygame.Rect(rectX, rectY, rectW, rectH)
    
    #assigns circle data to variables and makes shape a rectangle for hitbox purposes
    def makeCircle(self, circX, circY, circRad):
        self.x = circX
        self.y = circY
        self.rad = circRad
        self.shape = pygame.Rect(circX-7, circY-7, circRad, circRad)

    #updates coordinates based on velocity
    def setCords(self, xVelocity, yVelocity):
        self.x = self.x + xVelocity
        self.y = self.y + yVelocity
        self.shape = pygame.Rect(self.x-7, self.y-7, self.rad, self.rad)
        
    #getter methods
    def getCords(self):
        return (self.x, self.y, self.rad)
    

    def getObj(self):
        return self.shape
    
            