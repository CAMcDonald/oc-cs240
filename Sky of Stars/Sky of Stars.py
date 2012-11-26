## Sky Full of Stars

import random
import pygame

width, height = 800, 600


def init():
	width, height = 800, 600
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

		## Hunting for the width of the engine parts
		for i in range(raw_size[0]):
			color = image.get_at((i, 0))
			if color == colorkey:
				break
		width = i

		## Hunting for the height of the engine parts
		for i in range(raw_size[1]):
			color = image.get_at((0, i))
			if color == colorkey:
				break
		height = i 

		self.engines = image.subsurface((0, 0, width, height)).copy()

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
		print colorkey

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def update(self):
		f = self.frame / 2
		if f < 8:
			engine_part = f
		else:
			engine_part = 15 - f
		width = 24
		height = 28
		row = engine_part / 4 * height
		col = (engine_part % 4) * width
		engine =self.engines.subsurface((col, row, width, height))

		gap_x, gap_y = 46, 28
		self.image.blit(engine, (gap_x, gap_y))

		self.frame = (self.frame + 1) % 32
		return 
		d = random.randint(1,8)
		if d < 5:
			self.x += 2
		else:
			self.x += -2
		self.y += 1

def update(self):
	engine_part = self.fram / 20
	width = 24
	height = 28
	row = engine_part / 4 * height
	col = (engine_part % 4) * width
	engine =self.engines.subsurface((col, row, width, height))

	gap_x, gap_y = 156, 28
	self.image.blit(engine, (gap_x, gap_y))

	return 
	d = random.randint(1,8)
	if d < 5:
		self.x += 2
	else:
		self.x += -2
	self.y = 1

def load_UFO():
	UFO = pygame.image.load('UFO_2.jpg').convert()
	raw_size = UFO.get_size()

	# UFO = UFO.subsurface((0, 50, raw_size[0], raw_size[1]))
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
		clock.tick(20)

screen = init()
main(screen)