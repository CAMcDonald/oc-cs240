####### Cassie McDonald
####### Computer Science II
####### CS 240
####### Lab 1: Pygame

####### Program creates my artistic rendition of an Olympic Flag printed on a light blue background. 

import pygame

pygame.init()

## Set Screen Size
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

## Main Game Loop, continues until user exits
run = True
while run:
    ## Draws an Olympic Flag on a light blue background
    screen.fill((0, 191,255))                                       ## Deep Sky Blue background
    pygame.draw.rect(screen, (255, 255, 255), (120, 120, 400, 240)) ## Draws flag
    pygame.draw.circle(screen, (0, 0, 205), (200, 200), 50, 5)      ## Draws First Circle - Blue
    pygame.draw.circle(screen, (255, 255, 0), (255, 260), 50, 5)    ## Draws Second Circle - Yellow
    pygame.draw.circle(screen, (0, 0, 0), (310, 200), 50, 5)        ## Draws Third Circle - Black
    pygame.draw.circle(screen, (0, 100, 0), (365, 260), 50, 5)      ## Draws Fourth Circle - Green
    pygame.draw.circle(screen, (255, 0, 0), (415, 200), 50, 5)      ## Draws Fifth Circle - Red

    ## Flips to the surface
    pygame.display.flip()

    ## Exits program by hitting the 'x' or pushing q
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            run = False 
            
