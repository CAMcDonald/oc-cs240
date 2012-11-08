## Sky Full of Stars

import random
import pygame

width, height = 800, 600

def init():
    pygame.init()

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

def load_ship():
	ship = pygame.image.load('ship.png').convert()
	raw_size = ship.get_size()

	ship = ship.subsurface((0, 0, raw_size[0]/2, raw_size[1]/2))
	new_size = ship.get_size()

	ship = ship.subsurface((new_size[0]/2 - 10, new_size[1]/2, new_size[0]/2 + 10, new_size[1]/2))
	ship.set_colorkey((191, 220, 191))
	return ship

def load_UFO():
	UFO = pygame.image.load('UFO_2.jpg').convert()
	raw_size = UFO.get_size()

	UFO = UFO.subsurface((0, 0, raw_size[0]-25, raw_size[1]-75))
	new_size = UFO.get_size()

	UFO.set_colorkey((0, 0, 0))
	return UFO

def main(screen):
	running = True

	ship = load_ship()
	UFO = load_UFO()
	space = build_space(screen)

	while running:
		screen.blit(space, (0, 0))
		screen.blit(ship, (100, 100))
		screen.blit(UFO, (400, 250))
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
				running = False

screen = init()
main(screen)