import pygame 

class Ball(pygame.Rect):

    # Speed variables
    ball_speed_y = 0
    ball_speed_x = 0

    def setSpeedX(self, speedX):
        self.ball_speed_x = speedX

    def setSpeedY(self, speedY):
        self.ball_speed_y = speedY
    
    def getSpeedX(self):
        return self.ball_speed_x

    def getSpeedY(self):
        return self.ball_speed_y