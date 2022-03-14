import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption("Pygame Window")

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

player_image = pygame.image.load("player.png")


moving_left = False
moving_right = False

player_location = (50,50)

while True: # main game loop
	screen.blit(player_image, player_location)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				moving_right = True
			if event.key == K_LEFT:
				moving_left = True

		if event.type == KEYUP:
			if event.key == K_RIGHT:
				moving_right = False
			if event.key == K_LEFT:
				moving_left = False






	pygame.display.update()
	clock.tick(60)