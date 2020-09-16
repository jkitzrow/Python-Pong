import pygame

class Paddle(pygame.Rect):
    
    paddle_speed = 0

    def setSpeed(self, speed):
        self.paddle_speed = speed
    
    def getSpeed(self):
        return self.paddle_speed