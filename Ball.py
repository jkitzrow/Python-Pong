import pygame, random

class Ball(pygame.Rect):
    """
    Represents a ball in the game
    @param pygame.Rect: Extends the rectangle class in pygame
    """

    # Speed variables
    ball_speed_y = 7
    ball_speed_x = 7
    time_at_score = None

    def setSpeedX(self, speedX):
        """
        Sets the X speed of the ball
        @param speedX: The speed which is to be set for X
        """

        self.ball_speed_x = speedX

    def setSpeedY(self, speedY):
        """
        Sets the Y speed of the ball
        @param speedY: The speed which is to be set for Y
        """
        self.ball_speed_y = speedY
    
    def getSpeedX(self):
        """
        Gets the X speed of the ball
        @return: The X speed of the ball
        """

        return self.ball_speed_x

    def getSpeedY(self):
        """
        Gets the Y speed of the ball
        @return: The Y speed of the ball
        """

        return self.ball_speed_y
    
    def getTimeScore(self):
        """
        Gets the time at which the ball was scored
        @return: The time in milliseconds when the ball was scored
        """

        return self.time_at_score
    
    def setTimeScore(self, time):
        """
        Sets the time when the ball is scored
        @param time: The time to be set in milliseconds
        """

        self.time_at_score = time
    
    def ballCollision(self, width, height, player, opponent):
        """
        Determines if a ball collides with anything
        @param width: The width of the screen
        @param height: The height of the screen
        @param player: The player paddle
        @param opponent: The opponent paddle
        """

        self.x += self.getSpeedX()
        self.y += self.getSpeedY()

        # If ball hits top or bottom of window, reflect
        if self.top <= 0 or self.bottom >= height:
            self.setSpeedY(-self.getSpeedY())
        # If ball hits opponent side
        if self.left <= 0:
            player.scored()
            opponent.resetPosition(width, height, True)
            player.resetPosition(width, height, False)
            self.time_at_score = pygame.time.get_ticks()
        # If ball hits player side
        if self.right >= width:
            opponent.scored()
            opponent.resetPosition(width, height, True)
            player.resetPosition(width, height, False)
            self.time_at_score = pygame.time.get_ticks()
        # If ball hits a paddle
        if self.colliderect(player) or self.colliderect(opponent):
            self.setSpeedX(-self.getSpeedX())
    
    def reset(self, width, height, font, game):
        """
        Resets the ball to the middle of the game
        @param width: The width of the game screen
        @param height: The height of the game screen
        @param font: The font to use for the text
        @param game: The game instance
        """

        current_time = pygame.time.get_ticks()
        self.center = ((int)(width / 2), (int)(height / 2))

        # If still waiting, don't add speed
        if current_time - self.time_at_score < 3000:
            self.setSpeedX(0)
            self.setSpeedY(0)

            # Displays a countdown until ball is active again
            countdown_text = font.render("{}".format((int)(3 - (current_time - self.time_at_score) / 1000))
                , False, (0, 0, 0))
            game.blit(countdown_text, (self.x + 9, self.y + 3))


        # Not waiting
        else:
            self.setSpeedX(7 * random.choice((-1, 1)))
            self.setSpeedY(7 * random.choice((-1, 1)))
            self.time_at_score = None