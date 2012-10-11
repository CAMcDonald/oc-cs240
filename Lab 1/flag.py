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

class Olympic_Flag(object):
    """A class that shows an olympic flag and is pygame and pygame.Rect aware"""
    def __init__(self, left, top, width = 400, height = 240):
        self.rect = pygame.Rect(left, top, width, height)
        self.horizontal = 1
        self.vertical = 1
        ## Draws flag
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(white)

        ## Draws rings on flag
        rings = [((blue), (80, 80)), ((yellow), (135, 140)), ((black), (190, 80)), ((green), (245, 140)), ((red), (295, 80))] 
        for ring in rings:
            pygame.draw.circle(self.image, ring[0], ring[1], 50, 5)


    def draw(self, screen):
        ## Draws flag as single image. 
        screen.blit(self.image, self.rect)

    def update(self, screen):
        screen_width, screen_height = screen.get_size()
        self.rect.left += self.horizontal
        self.rect.top += self.vertical
        if self.rect.right > screen_width:
            self.horizontal = -self.horizontal
        elif self.rect.left < 0:
            self.horizontal = -self.horizontal
        if self.rect.top < 0:
            self.vertical = -self.vertical
        elif self.rect.bottom > screen_height:
            self.vertical = -self.vertical

class Ball(object):
    """Draws a ball that is pygame and pygame.Rect aware"""
    def __init__(self, x, y, radius):
        self.rect = pygame.Rect(0, 0, 2*radius, 2*radius)
        self.rect.center = (x, y)
        self.horizontal = 5
        self.vertical = 5
        ## Draws ball on rectangle
        self.image = pygame.Surface(self.rect.size)
        self.image.fill((0, 191, 255))

        ## Draws ball on rectangle surface
        pygame.draw.circle(self.image, black, (radius, radius), 50)


    def draw(self, screen):
        ## Draws ball as single image. 
        screen.blit(self.image, self.rect)

    def update(self, screen):
        screen_width, screen_height = screen.get_size()
        self.rect.left += self.horizontal
        self.rect.top += self.vertical
        if self.rect.right > screen_width:
            self.horizontal = -self.horizontal
        elif self.rect.left < 0:
            self.horizontal = -self.horizontal
        if self.rect.top < 0:
            self.vertical = -self.vertical
        elif self.rect.bottom > screen_height:
            self.vertical = -self.vertical

class Picture(object):
    """Inserts a picture of Michael Phelps in the background"""
    def insert(self, screen):
        ## Inserts the picture into the file
        Michael = pygame.image.load(Michael.jpg).convert_alpha()
        Michael_rect = Michael.get_rect()