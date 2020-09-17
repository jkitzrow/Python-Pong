import pygame, random

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
        if self.left <= 0:
            player.scored()
            self.reset(width, height)
        if self.right >= width:
            opponent.scored()
            self.reset(width, height)
        if self.colliderect(player) or self.colliderect(opponent):
            self.setSpeedX(-self.getSpeedX())
    
    def reset(self, width, height):
        self.center = ((int)(width / 2), (int)(height / 2))

        self.setSpeedX(7 * random.choice((-1, 1)))
        self.setSpeedY(7 * random.choice((-1, 1)))