import pygame, random

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

# Main game loop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False
        

pygame.quit()
quit()
