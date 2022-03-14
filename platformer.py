import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption("Pygame Window")

WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
TILE_SIZE = 16
display = pygame.Surface((300,200))

player_image = pygame.image.load("images/player2.png")
player_image.set_colorkey((255, 255, 255))
tile1_image = pygame.image.load("images/tile.png")

game_map = ["00000011100000000000",
			"00000000000000000000",
			"00000000000000000000",
			"00000000000000000000",
			"00000000000000000000",
			"00000000000000000000",
			"00000000000000000000",
			"00000000000000000000",
			"00000111100000000000",
			"00001000000000000000",
			"00111111100000000000",
			"11111111111111110000",
			"11111111111111110000"]
for i in range(len(game_map)):
	game_map[i] = [int(tile) for tile in game_map[i]]

def collision_test(rect, tiles):
	hit_list = []
	for tile in tiles:
		if rect.colliderect(tile):
			hit_list.append(tile)
	
	return hit_list

def move(rect, movement, tiles):
	collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False, }
	rect.x += movement[0]
	hit_list = collision_test(rect, tiles)
	for tile in hit_list:
		if movement[0] > 0:
			rect.right = tile.left
			collision_types['right'] = True
		elif movement[0] < 0:
			rect.left = tile.right
			collision_types['left'] = True

	rect.y += movement[1]
	hit_list = collision_test(rect, tiles)
	for tile in hit_list:
		if movement[1] > 0:
			rect.bottom = tile.top
			collision_types['bottom'] = True
		elif movement[1] < 0:
			rect.top = tile.bottom
			collision_types['top'] = True

	return rect, collision_types



moving_left = False
moving_right = False

air_timer = 0
player_y_momentum = 0

player_rect = pygame.Rect(50, 50, player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(50,50, 100, 100)

while True: # main game loop
#displaying stuff
	display.fill((146, 244, 255))
	

	tile_rects = []
	for i in range(len(game_map)):
		for j in range(len(game_map[0])):
			if game_map[i][j] == 1:
				display.blit(tile1_image, (j*TILE_SIZE, i*TILE_SIZE))
			if game_map[i][j] != 0:
				tile_rects.append(pygame.Rect(j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE))


#movement
	player_movement = [0,0]
	if moving_right:
		player_movement[0] += 2
	elif moving_left:
		player_movement[0] += -2

	player_movement[1] += player_y_momentum
	player_y_momentum += .2
	if player_y_momentum >3:
		player_y_momentum = 3


	player_rect, collisions = move(player_rect, player_movement, tile_rects)
	if collisions['bottom']:
		player_y_momentum = 0
	if collisions['top']:
		player_y_momentum = 0

	if collisions['bottom']:
		player_y_momentum = 0
		air_timer = 0
	else:
		air_timer += 1
	



	display.blit(player_image, (player_rect.x, player_rect.y))

#Checking for input
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				moving_right = True
			if event.key == K_LEFT:
				moving_left = True
			if event.key == K_UP:
				if air_timer < 6:
					player_y_momentum = -5
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				moving_right = False
			if event.key == K_LEFT:
				moving_left = False





	surf = pygame.transform.scale(display, WINDOW_SIZE, screen)
	screen.blit(surf, (0,0))
	pygame.display.update()
	clock.tick(60)