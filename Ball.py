import pygame, random

class Ball(pygame.Rect):

    # Speed variables
    ball_speed_y = 7
    ball_speed_x = 7
    time_at_score = None

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
            self.time_at_score = pygame.time.get_ticks()
            #self.reset(width, height)
        if self.right >= width:
            opponent.scored()
            self.time_at_score = pygame.time.get_ticks()
            #self.reset(width, height)
        if self.colliderect(player) or self.colliderect(opponent):
            self.setSpeedX(-self.getSpeedX())
    
    def reset(self, width, height):
        current_time = pygame.time.get_ticks()
        self.center = ((int)(width / 2), (int)(height / 2))

        if current_time - self.time_at_score < 2100:
            self.setSpeedX(0)
            self.setSpeedY(0)

        else:
            self.setSpeedX(7 * random.choice((-1, 1)))
            self.setSpeedY(7 * random.choice((-1, 1)))
            self.time_at_score = None