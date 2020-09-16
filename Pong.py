import pygame, random
from Paddle import Paddle
from Ball import Ball

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Screen variables and configuration
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
game = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Color variables
bg_color = (0, 0, 0)
paddle_color = (255, 255, 255)

# Create player, opponent, and ball
ball = Ball((int)(SCREEN_WIDTH / 2 - 15), (int)(SCREEN_HEIGHT / 2 - 15), 30, 30)
player = Paddle(SCREEN_WIDTH - 20, (int)(SCREEN_HEIGHT / 2 - 70), 10, 140)
opponent = Paddle(10, (int)(SCREEN_HEIGHT / 2 - 70), 10, 140)

# Main game loop
run = True
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
        # If user releases movement key, reset speed to 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player.setSpeed(0)
    
    # Adds speed and checks for collisions
    player.paddleCollision(SCREEN_HEIGHT, False, ball)
    opponent.paddleCollision(SCREEN_HEIGHT, True, ball)

    # Draws all objects on screen
    game.fill(bg_color)
    pygame.draw.rect(game, paddle_color, player)
    pygame.draw.rect(game, paddle_color, opponent)
    pygame.draw.rect(game, paddle_color, ball)

    # Update screen 90 times every second
    pygame.display.update()
    clock.tick(90)

pygame.quit()
quit()
