import pygame, sys, random
from model import Model
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screenColor = (0, 0, 0)
circColor = (255, 255, 255)
rectColor = (0, 255, 21)
rectSpeed = 7

    
class Controller:
    def __init__(self, v):
        self.view = v
        self.clock = pygame.time.Clock()


    def startGame(self):
        p1 = Model()
        p2 = Model()
        p1.makeRect(20, 250, 15, 90)
        p2.makeRect(965, 250, 15, 90)
        
        ball = Model()
        ball.makeCircle(500, 300, 10)
        ballV = (-5, 5)
        self.p1Points = 0
        self.p2Points = 0
        
        resetGame = False
        while True:
                
                
            for event in self.view.getEvents():
                if event.type == pygame.QUIT:
                    self.view.endGame()
                    sys.exit()
                    
            self.checkWin()
            
            if resetGame:
                resetGame = False
                ball.makeCircle(500, 300, 10)
                ballV = (5 * random.choice([-1,1]), 5 * random.choice([-1,1]))
                pygame.time.delay(300)
                p1.makeRect(20, 250, 15, 90)
                p2.makeRect(965, 250, 15, 90)
                
        
            self.moveRect1(p1.getObj())        
            self.moveRect2(p2.getObj())
            self.moveCirc(ball, ballV)
            
            
            if ball.getObj().top <= 0 or ball.getObj().bottom >= SCREEN_HEIGHT:
                ballV = (ballV[0], ballV[1]*-1)
                
                
            if(ball.getObj().left <= 0 or ball.getObj().right >= SCREEN_WIDTH):
                if ball.getObj().left <= 0:
                    self.p2Points += 1
                else:
                    self.p1Points += 1
                resetGame = True
            
            
            if ball.getObj().colliderect(p1.getObj()):
                ballV = (ballV[0]*-1, ballV[1])
            elif ball.getObj().colliderect(p2.getObj()):
                ballV = (ballV[0]*-1, ballV[1])      
                
              
            self.view.backgroundFill(screenColor)
            
            self.view.drawRect(rectColor, p1.getObj())
            self.view.drawRect(rectColor, p2.getObj())
            self.view.drawCirc(circColor, ball.getCords())
            
            self.view.update()
            self.clock.tick(60)
            
            
    def checkWin(self):
        if self.p1Points >= 3:
            print("\n\nPlayer 1 Win!!\n\n")
            pygame.time.delay(300)
            self.view.endGame()
            sys.exit()
        elif self.p2Points >= 3:
            print("\n\nPlayer 2 Win!!\n\n")
            pygame.time.delay(300)
            self.view.endGame()
            sys.exit()

 
    def moveCirc(self, ball, velocity):
        ball.setCords(velocity[0], velocity[1])
 
 
    def moveRect1(self, rect):
        keys = self.view.getPressed()
        if keys[pygame.K_s] :
            rect.move_ip(0, rectSpeed)
        elif keys[pygame.K_w]:
            rect.move_ip(0, -rectSpeed)  
        rect.clamp_ip(0,0, SCREEN_WIDTH, SCREEN_HEIGHT) 

    def moveRect2(self, rect):
            keys = self.view.getPressed()
            if keys[pygame.K_DOWN] :
                rect.move_ip(0, rectSpeed)
            elif keys[pygame.K_UP]:
                rect.move_ip(0, -rectSpeed)  
            rect.clamp_ip(0,0, SCREEN_WIDTH, SCREEN_HEIGHT) 