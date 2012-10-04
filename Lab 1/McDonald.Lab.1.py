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
    horizontal, vertical = 1, 1
    flag1 = flag.Flag(0, 0)
    flag2 = flag.Flag(240,240)

    


    ## Main Game Loop, continues until user exits
    run = True
    while run:
               
        ## Draws an Olympic Flag on a light blue background
        screen.fill((0, 191,255))                                               ## Deep Sky Blue background
        flag1.draw(screen)                                                      ## Draws Flag
        flag2.draw(screen)
        pygame.display.flip()                                                   ## Flips to the surface
       

        ## Exits program by hitting the 'x' or pushing q
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                run = False 
            

screen = init()
main(screen)