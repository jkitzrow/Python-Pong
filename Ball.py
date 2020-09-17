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
    
    def getTimeScore(self):
        return self.time_at_score
    
    def ballCollision(self, width, height, player, opponent):
        self.x += self.getSpeedX()
        self.y += self.getSpeedY()

        # If ball hits top or bottom of window, reflect
        if self.top <= 0 or self.bottom >= height:
            self.setSpeedY(-self.getSpeedY())
        # If ball hits opponent side
        if self.left <= 0:
            player.scored()
            self.time_at_score = pygame.time.get_ticks()
        # If ball hits player side
        if self.right >= width:
            opponent.scored()
            self.time_at_score = pygame.time.get_ticks()
        # If ball hits a paddle
        if self.colliderect(player) or self.colliderect(opponent):
            self.setSpeedX(-self.getSpeedX())
    
    def reset(self, width, height, font, game):
        current_time = pygame.time.get_ticks()
        self.center = ((int)(width / 2), (int)(height / 2))

        # If still waiting, don't add speed
        if current_time - self.time_at_score < 3000:
            self.setSpeedX(0)
            self.setSpeedY(0)

            # Displays a countdown until ball is active again
            countdown_text = font.render(f"{(int)(4 - (current_time - self.time_at_score) / 1000)}"
                , False, (0, 0, 0))
            game.blit(countdown_text, (self.x + 9, self.y + 3))


        # Not waiting
        else:
            self.setSpeedX(7 * random.choice((-1, 1)))
            self.setSpeedY(7 * random.choice((-1, 1)))
            self.time_at_score = None