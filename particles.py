import pygame, sys
import random as rd
from classes import *

mainClock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500,500), 0, 32)






particles = []
    
gravity = .05

while True:

    screen.fill((0,0,0))
    particles.append(Particle(
            (250, 250), [rd.randint(0,20)/10 -1, rd.randint(0,20)/10 -1],
             rd.randint(5,8),
             (rd.randint(0, 255), rd.randint(0, 255),rd.randint(0, 255))
             ))
    
    for particle in particles:
        particle.render(screen)
        if particle.radius <= 0:
            particles.remove(particle)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print(len(particles))
                pygame.quit()
                sys.exit()

    pygame.display.update()
    mainClock.tick(60)