import pygame, random

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Main game loop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False
        

pygame.quit()
quit()
