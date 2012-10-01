import pygame

class Flag(object):
    def __init__(self, left, top):
        self.left = left
        self.top = top
        self.width = 400
        self.height = 240


    def draw(self, screen):
        ## Colors of Rings and Flag
        white = pygame.Color(255, 255, 255) 
        blue = pygame.Color(0, 0, 205)
        yellow = pygame.Color(255, 255, 0)
        black = pygame.Color(0, 0, 0)
        green = pygame.Color(0, 100, 0)
        red = pygame.Color(255, 0, 0)

        ## Draws an Olympic Flag 
        pygame.draw.rect(screen, white, (self.left, self.top, self.width, self.height) )
        pygame.draw.circle(screen, blue, (self.left + 80, self.top + 80), 50, 5)              ## Draws First Circle - Blue
        pygame.draw.circle(screen, yellow, (self.left + 135, self.top + 140), 50, 5)          ## Draws Second Circle - Yellow
        pygame.draw.circle(screen, black, (self.left + 190, self.top + 80), 50, 5)            ## Draws Third Circle - Black
        pygame.draw.circle(screen, green, (self.left + 245, self.top + 140), 50, 5)           ## Draws Fourth Circle - Green
        pygame.draw.circle(screen, red, (self.left + 295, self.top + 80), 50, 5)              ## Draws Fifth Circle - Red