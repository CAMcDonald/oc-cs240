## Sky Full of Stars

import random
import pygame

window_title = "Sky of Stars"
width, height = 800, 600


def init():
    width, height = 800, 600
    pygame.init()

    pygame.display.set_caption(window_title)

    ## Set Screen Size
    return pygame.display.set_mode((width, height))

def draw_space(screen, stars):
    screen.fill((0, 0, 0))
    for s in stars:
        if s[2] == 3:
            star = pygame.Color(255, 255, 255)
        elif s[2] == 2:
            star = pygame.Color(200, 200, 255)
        elif s[2] == 1:
            star = pygame.Color(255, 170, 170)
        pygame.draw.circle(screen, star, s[:2], s[2])

def build_space(screen):
    space = screen.copy()
    width, height = screen.get_size()

    stars = []
    for star in range(60):
        x = random.randint(0,width)
        y = random.randint(0, height)
        rand = random.randint(1, 10)
        if rand <= 6:
            r = 1
        elif rand <= 9:
            r = 2
        else:
            r = 3 
        stars.append((x, y, r))
    
    draw_space(space, stars)
    return space

class NewShip(object):
    def __init__(self):
        image = pygame.image.load('ship.png').convert()
        raw_size = image.get_size()
        self.image = image.subsurface((110, 0, raw_size[0] - 110, raw_size[1] - 110))
        self.x = 100
        self.y = 0
        self.size = self.image.get_size()
        colorkey = self.image.get_at((self.size[0] -1, self.size[1] - 1))
        self.frame =  0
        self.velocity = 0
        self.bullets = []
        self.animatedoor = False
        self.dooropen = False

        self.parts = []
        width = 24
        height = 28
        for engine_part in range(8):            
            row = engine_part / 4 * height
            col = (engine_part % 4) * width
            self.parts.append(image.subsurface((col, row, width, height)).copy())

    
        ## Finding the horizontal location of engine gap
        seen_ck = False
        past_grid = False
        for i in range(raw_size[0]):
            color = image.get_at((i, 50))
            if color == colorkey:
                seen_ck = True
                if past_grid:
                    break

            if color != colorkey and seen_ck:
                past_grid = True
        gap_x = i - 110

        ## Finding the vertical location of engine gap
        seen_ship = False
        for i in range(raw_size[1]):
            color - image.get_at((gap_x + 1, i))
            if color != colorkey:
                seen_ship = True
            if color == colorkey and seen_ship:
                break
        gap_y = i

        self.image.set_colorkey(colorkey)
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullets:
            pygame.draw.circle(screen, (255, 255, 255), (bullet[0], bullet[1]), 4)

    def move_x(self, delta):
        self.x += delta

    def move_y(self, delta):
        self.y += delta

    def update(self):
        f = self.frame / 2
        engine_part = f

        gap_x, gap_y = 46, 28
        # self.image.blit(self.parts[engine_part], (gap_x, gap_y))

        if self.animatedoor:
            self.frame = (self.frame + 1)
            if self.frame == 16:
                self.frame = 0
                self.animatedoor = False
                self.dooropen = not self.dooropen
            self.image.blit(self.parts[engine_part], (gap_x, gap_y))
        else: 
            if self.dooropen:
                self.image.blit(self.parts[7], (gap_x, gap_y))
            else:
                self.image.blit(self.parts[0], (gap_x, gap_y))
                

        remove = False
        # Move any existing bullets
        for bullet in self.bullets:
            bullet[1] += 10
            if bullet[0] > screen.get_width():
                remove = True

        # Delete any offscreen bullets
        if remove:
            del self.bullets[0]

    def shoot(self):
        if len(self.bullets) < 9:
            y_loc = self.y + 120
            x_loc = self.x + 60
            self.bullets.append([x_loc, y_loc])
            

def load_UFO():
        UFO = pygame.image.load('UFO_2.jpg').convert()
        raw_size = UFO.get_size()

        new_size = UFO.get_size()

        UFO.set_colorkey(UFO.get_at((0,raw_size[1]-1)))
        return UFO

def main(screen):
    running = True

    ship = NewShip()
    UFO = load_UFO()
    space = build_space(screen)

    clock = pygame.time.Clock()

    while running:
        screen.blit(space, (0, 0))
        ship.draw(screen)
        ship.update()
        screen.blit(UFO, (400, 250))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                running = False

        
        if event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if event.key == pygame.K_LEFT:
                ship.move_x(-10)
            if event.key == pygame.K_RIGHT:
                ship.move_x(10)
            if event.key == pygame.K_DOWN:
                ship.move_y(10)
            if event.key == pygame.K_UP:
                ship.move_y(-10)
            if event.key == pygame.K_SPACE:
                ship.shoot()
            if event.key == pygame.K_d:
                ship.animatedoor = True

        clock.tick(20)

screen = init()
main(screen)
