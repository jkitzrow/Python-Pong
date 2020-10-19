import pygame

class Paddle(pygame.Rect):
    """
    Represents a paddle in the game
    @param pygame.Rect: Extends the rectangle class in pygame
    """
    
    paddle_speed = 0
    paddle_score = 0

    def setSpeed(self, speed):
        """
        Sets the paddle speed
        @param speed: The speed to set
        """

        self.paddle_speed = speed
    
    def getSpeed(self):
        """
        Gets the current paddle speed
        @return: The current paddle speed
        """

        return self.paddle_speed
    
    def paddleCollision(self, height, isAi, ball):
        """
        Determines if the paddle collides with anything
        @param height: The height of the game screen
        @param isAi: A boolean which tells if the paddle is ai or the player
        @param ball: The instance of the ball object in the game
        """

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
        """
        Gets the current score for the paddle
        @return: The current score for the paddle
        """

        return self.paddle_score
    
    def scored(self):
        """
        Increments the score of the paddle
        """

        self.paddle_score += 1
    
    def resetScore(self):
        """
        Resets the paddle's score
        """

        self.paddle_score = 0
    
    def resetPosition(self, width, height, isAi):
        """
        Resets the position of the paddle
        @param width: The width of the game screen
        @param height: The height of the game screen
        @param isAi: Boolean which determines if the paddle is ai or the player
        """

        if not isAi:
            self.x = width - 20
            self.y = (int)(height / 2 - 70)
        else:
            self.x = 10
            self.y = (int)(height / 2 - 70)

    def updateScore(self, font, game, width, height, isAi):
        """
        Updates the score on the screen
        @param font: The font to use for the score
        @param game: An instance of the game
        @param width: The width of the game screen
        @param height: The height of the game screen
        @param isAi: Boolean which determines if the paddle is ai or the player
        @return: Returns whether the game is over or not
        """

        # Sets up the score text
        paddle_text = font.render("{}".format(self.getScore()), False, (255, 255, 255))
        end_font = pygame.font.SysFont("Arialbd", 60)

        # If paddle is Ai, display ai score
        if isAi:
            game.blit(paddle_text, ((int)(width / 2 - 40), 20))
        # If paddle is player, display player score
        else:
            game.blit(paddle_text, ((int)(width / 2 + 30), 20))

        # If player wins, display win screen
        if self.getScore() == 5 and not isAi:
            game_over_text = end_font.render("Game Over. You Win!", False, (0, 0, 0))
            restart_text = end_font.render("Press (R) to restart, or (ESC) to exit.", False, (0, 0, 0))
            game.fill((255, 255, 255))
            game.blit(game_over_text, ((int)(width / 3 - 40), ((int)(height / 2 - 60))))
            game.blit(restart_text, ((int)(width / 3 - 180), ((int)(height / 2 + 60))))
            
            return True
        # If player loses, display losing screen
        elif self.getScore() == 5 and isAi:
            game_over_text = end_font.render("Game Over. You Lose!", False, (0, 0, 0))
            restart_text = end_font.render("Press (R) to restart, or (ESC) to exit.", False, (0, 0, 0))
            game.fill((255, 255, 255))
            game.blit(game_over_text, ((int)(width / 3 - 40), ((int)(height / 2 - 60))))
            game.blit(restart_text, ((int)(width / 3 - 180), ((int)(height / 2 + 60))))
            
            return True
        
        return False