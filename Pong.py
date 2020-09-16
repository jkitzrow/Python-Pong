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
ball = Ball()
player = Paddle()
opponent = Paddle()

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
                player.setSPeed(7)
            if event.key == pygame.K_ESCAPE: # Press Escape key to close game
                run = False
        # If user releases movement key, reset speed to 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player.setSpeed(0)
        

pygame.quit()
quit()
