import pygame

class Paddle(pygame.Rect):
    
    paddle_speed = 0
    paddle_score = 0

    def setSpeed(self, speed):
        self.paddle_speed = speed
    
    def getSpeed(self):
        return self.paddle_speed
    
    def paddleCollision(self, height, isAi, ball):
        # If paddle is player
        if not isAi:
            self.y += self.getSpeed()

            # Make sure in screen bounds
            if self.top <= 0:
                self.top = 0
            if self.bottom >= height:
                self.bottom = height
        
        # If paddle is Ai
        else:
            # Predict where ball is going
            if self.top < ball.y:
                self.top += 9
            if self.bottom > ball.y:
                self.bottom -= 9
            # Make sure in screen bounds
            if self.top <= 0:
                self.top = 0
            if self.bottom >= height:
                self.bottom = height

    def getScore(self):
        return self.paddle_score
    
    def scored(self):
        self.paddle_score += 1
    
    def resetScore(self):
        self.paddle_score = 0
    
    def resetPosition(self, width, height, isAi):
        if not isAi:
            self.x = width - 20
            self.y = (int)(height / 2 - 70)
        else:
            self.x = 10
            self.y = (int)(height / 2 - 70)

    def updateScore(self, font, game, width, height, isAi):
        paddle_text = font.render("{}".format(self.getScore()), False, (255, 255, 255))
        end_font = pygame.font.SysFont("Arialbd", 60)

        if isAi:
            game.blit(paddle_text, ((int)(width / 2 - 40), 20))
        else:
            game.blit(paddle_text, ((int)(width / 2 + 30), 20))

        if self.getScore() == 5 and not isAi:
            game_over_text = end_font.render("Game Over. You Win!", False, (0, 0, 0))
            restart_text = end_font.render("Press (R) to restart, or (ESC) to exit.", False, (0, 0, 0))
            game.fill((255, 255, 255))
            game.blit(game_over_text, ((int)(width / 3 - 40), ((int)(height / 2 - 60))))
            game.blit(restart_text, ((int)(width / 3 - 180), ((int)(height / 2 + 60))))
            
            return True

        elif self.getScore() == 5 and isAi:
            game_over_text = end_font.render("Game Over. You Lose!", False, (0, 0, 0))
            restart_text = end_font.render("Press (R) to restart, or (ESC) to exit.", False, (0, 0, 0))
            game.fill((255, 255, 255))
            game.blit(game_over_text, ((int)(width / 3 - 40), ((int)(height / 2 - 60))))
            game.blit(restart_text, ((int)(width / 3 - 180), ((int)(height / 2 + 60))))
            
            return True
        
        return False