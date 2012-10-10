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
    flag1 = flag.Flag(0, 0)
    flag2 = flag.Flag(100, 200)
    


    ## Main Game Loop, continues until user exits
    run = True
    while run:
               
        ## Draws an Olympic Flag on a light blue background
        screen.fill((0, 191,255))                                               ## Deep Sky Blue background
        flag1.draw(screen)                                                      ## Draws Flag
        flag1.update(screen)
        flag2.draw(screen)
        flag2.update(screen)
        pygame.display.flip()                                                   ## Flips to the surface
       

        ## Exits program by hitting the 'x' or pushing q
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                run = False 
            
        clock.tick(50)
        
screen = init()
main(screen)