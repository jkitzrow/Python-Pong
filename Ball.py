import pygame 

class Ball(pygame.Rect):

    # Speed variables
    ball_speed_y = 7
    ball_speed_x = 7

    def setSpeedX(self, speedX):
        self.ball_speed_x = speedX

    def setSpeedY(self, speedY):
        self.ball_speed_y = speedY
    
    def getSpeedX(self):
        return self.ball_speed_x

    def getSpeedY(self):
        return self.ball_speed_y
    
    def ballCollision(self, width, height, player, opponent):
        self.x += self.getSpeedX()
        self.y += self.getSpeedY()

        if self.top <= 0 or self.bottom >= height:
            self.setSpeedY(-self.getSpeedY())
        if self.left <= 0 or self.right >= width:
            self.setSpeedX(-self.getSpeedX())
        if self.colliderect(player) or self.colliderect(opponent):
            self.setSpeedX(-self.getSpeedX())