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
                self.top += 7
            if self.bottom > ball.y:
                self.bottom -= 7
            # Make sure in screen bounds
            if self.top <= 0:
                self.top = 0
            if self.bottom >= height:
                self.bottom = height

    def getScore(self):
        return self.paddle_score
    
    def scored(self):
        self.paddle_score += 1

    def updateScore(self, font, game, width, isAi):
        paddle_text = font.render("{}".format(self.getScore()), False, (255, 255, 255))

        if isAi:
            game.blit(paddle_text, ((int)(width / 2 - 40), 20))
        else:
            game.blit(paddle_text, ((int)(width / 2 + 30), 20))