import pygame

## Colors that need to be used for the program to draw a flag
white = pygame.Color(255, 255, 255) 
blue = pygame.Color(0, 0, 205)
yellow = pygame.Color(255, 255, 0)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 100, 0)
red = pygame.Color(255, 0, 0)

class Rect(object):
    def __init__(self, left, top, width, height):
        ## Given parameters
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        ## Calculated parameters
        self.right = self.left + self.width
        self.bottown = self.top + self.height

    def move_ip(self, xoffset, yoffset):
        self.left += xoffset
        self.top += yoffset

         ## Calculated parameters
        self.right = self.left + self.width
        self.bottown = self.top + self.height

    def move(self, xoffset, yoffset):
        return Rect(self.left + xoffset, self.top + yoffset, self.width, self.height)

    def top_left(self):
        return (self.top, self.left)

class Flag(object):
    """A Class that shows and olympic flag"""
    def __init__(self, left, top):
        self.left = left
        self.top = top
        self.width = 400
        self.height = 240

    def draw(self, screen):
        """Draws an olympic flag at left and top locations"""
        ## Draws an Olympic Flag 
        pygame.draw.rect(screen, white, (self.left, self.top, self.width, self.height) )
        pygame.draw.circle(screen, blue, (self.left + 80, self.top + 80), 50, 5)              ## Draws First Circle - Blue
        pygame.draw.circle(screen, yellow, (self.left + 135, self.top + 140), 50, 5)          ## Draws Second Circle - Yellow
        pygame.draw.circle(screen, black, (self.left + 190, self.top + 80), 50, 5)            ## Draws Third Circle - Black
        pygame.draw.circle(screen, green, (self.left + 245, self.top + 140), 50, 5)           ## Draws Fourth Circle - Green
        pygame.draw.circle(screen, red, (self.left + 295, self.top + 80), 50, 5)              ## Draws Fifth Circle - Red

class Flag2(object):
    """A class that shows an olympic flag and is pygame and Rect aware"""
    def __init__(self, left, top):
        self.rect = Rect(left, top, 400, 240)

    def draw(self, screen):
        """Draws an olympic flag at left and top locations"""
        ## Draws an Olympic Flag 
        pygame.draw.rect(screen, white, self.rect)
        rect = self.rect.move(80, 80)
        pygame.draw.circle(screen, blue, ring.top_left(), 50, 5)
        rect = self.rect.move(135, 140)
        pygame.draw.circle(screen, yellow, ring.top_left(), 50, 5)
        rect = self.rect.move(190, 80)
        pygame.draw.circle(screen, black, ring.top_left(), 50, 5)
        rect = self.rect.move(245, 140)
        pygame.draw.circle(screen, blue, ring.top_left(), 50, 5)
        rect = self.rect.move(295, 80)
        pygame.draw.circle(screen, blue, ring.top_left(), 50, 5)
