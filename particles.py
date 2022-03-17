import pygame, sys
import random

mainClock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500,500), 0, 32)



#particles = [location, velocity, time]
particles = []
gravity = .05


while True:

    screen.fill((0,0,0))

    #making particles
    particles.append([[250,250], [random.randint(0,20)/10 -1, random.randint(0,20)/10 -6], random.randint(4,6)])

    for particle in particles:
        particle[1][1] += gravity
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] += -.1
        pygame.draw.circle((screen), (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    mainClock.tick(60)