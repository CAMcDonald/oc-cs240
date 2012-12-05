####### Cassie McDonald
####### Computer Science II
####### CS 240
####### Lab 1: Pygame

####### Program creates my artistic rendition of an Olympic Flag printed on a light blue background.

import pygame
import flag

width, height = 640, 480

def init():
    pygame.init()

    ## Set Screen Size
    return pygame.display.set_mode((width, height))

def main(screen):
    ## Create clock
    clock = pygame.time.Clock()

    horizontal, vertical = 1, 1
    flag1 = flag.Olympic_Flag(50, 50)
    ball = flag.Ball(120, 240, 50)
    


    ## Main Game Loop, continues until user exits
    run = True
    while run:
               
        ## Draws an Olympic Flag on a light blue background
        screen.fill((0, 191,255))                                               ## Deep Sky Blue background
        ball.draw(screen)
        flag1.draw(screen)                                                      ## Draws Flag
        pygame.display.flip()                                                   ## Flips to the surface
        ball.update(screen)
        flag1.update(screen)

        ## Exits program by hitting the 'x' or pushing q
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                run = False 
            
        clock.tick(100)

screen = init()
main(screen)