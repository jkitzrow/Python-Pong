import pygame, random
from Paddle import Paddle
from Ball import Ball

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Screen variables and configuration
SCREEN_WIDTH = 980
SCREEN_HEIGHT = 660
game = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Color variables
bg_color = (0, 0, 0)
paddle_color = (255, 255, 255)

# Create player, opponent, and ball
ball = Ball((int)(SCREEN_WIDTH / 2 - 15), (int)(SCREEN_HEIGHT / 2 - 15), 30, 30)
player = Paddle(SCREEN_WIDTH - 20, (int)(SCREEN_HEIGHT / 2 - 70), 10, 140)
opponent = Paddle(10, (int)(SCREEN_HEIGHT / 2 - 70), 10, 140)

# Score related variables
font = pygame.font.SysFont("Arialbd", 40)

# Main game loop
run = True
game_over = False
while run:

    for event in pygame.event.get():
        # If user exits out of window
        if event.type == pygame.QUIT:
            run = False
        # If up or down button pressed, move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.setSpeed(-7)
            if event.key == pygame.K_DOWN:
                player.setSpeed(7)
            if event.key == pygame.K_ESCAPE: # Press Escape key to close game
                run = False
            if event.key == pygame.K_r and game_over == True:
                game_over = False
                player.resetScore()
                opponent.resetScore()
                ball.setTimeScore(pygame.time.get_ticks())
                ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT, font, game)
        # If user releases movement key, reset speed to 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player.setSpeed(0)
    
    # Adds speed and checks for collisions
    ball.ballCollision(SCREEN_WIDTH, SCREEN_HEIGHT, player, opponent)
    player.paddleCollision(SCREEN_HEIGHT, False, ball)
    opponent.paddleCollision(SCREEN_HEIGHT, True, ball)

    # Draws all objects on screen
    game.fill(bg_color)
    pygame.draw.rect(game, paddle_color, player)
    pygame.draw.rect(game, paddle_color, opponent)
    pygame.draw.rect(game, paddle_color, ball)
    pygame.draw.aaline(game, paddle_color, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    # If somebody scored, hold ball for 2 seconds, then reset
    if ball.getTimeScore() != None:
        ball.reset(SCREEN_WIDTH, SCREEN_HEIGHT, font, game)

    # Updates scores
    if player.updateScore(font, game, SCREEN_WIDTH, SCREEN_HEIGHT, False) or opponent.updateScore(font, game, SCREEN_WIDTH, SCREEN_HEIGHT ,True):
        game_over = True

    # Update screen 90 times every second
    pygame.display.update()
    clock.tick(90)

pygame.quit()
quit()
