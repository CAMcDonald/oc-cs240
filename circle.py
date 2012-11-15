

import pygame

WINDOW_TITLE = 'The Circle'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def init():
	pygame.init()
	pygame.display.set_caption(WINDOW_TITLE)

	return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def main(screen):
	x = WINDOW_WIDTH / 2
	y = WINDOW_HEIGHT / 2
	d = 5
	r, g, b = (255, 255, 255)

	running = True
	while running:
		screen.fill((0, 0, 0))

		pygame.draw.circle(screen, (r, g, b), (x, y), d)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
				running = False

			if event.type == pygame.KEYDOWN:
				mods = pygame.key.get_mods()
				if event.key == pygame.K_LEFT:
					x += -10
				if event.key == pygame.K_RIGHT:
					x += 10
				if event.key == pygame.K_DOWN:
					y += 10
				if event.key == pygame.K_UP:
					y += -10
				if event.key == pygame.K_EQUALS and mods & pygame.KMOD_SHIFT:
					d += 1
				if event.key == pygame.K_MINUS:
					d += -1
					if d < 0:
						d = 0
				if event.key == pygame.K_r:
					if mods & pygame.KMOD_SHIFT:
						r = min(255, r + 8)
					else:
						r = max(0, r - 8)
				if event.key == pygame.K_g:
					if mods & pygame.KMOD_SHIFT:
						g = min(255, g + 8)
					else:
						g = max(0, g - 8)
				if event.key == pygame.K_b:
					if mods & pygame.KMOD_SHIFT:
						b = min(255, b + 8)
					else:
						b = max(0, b - 8)


screen = init()
main(screen)