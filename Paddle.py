import pygame

class Paddle(pygame.Rect):
    
    paddle_speed = 0

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