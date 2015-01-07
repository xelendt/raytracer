import pygame
import time, sys

xres = 1000
yres = 800

pygame.init()
win = pygame.display.set_mode((xres, yres), pygame.SRCALPHA)


def event(e):
	if e.type == pygame.QUIT:
		sys.exit(0)

def draw():
	pygame.display.update()
	pygame.display.flip()

while True:
	win.fill((255, 255, 255))

	for e in pygame.event.get():
		event(e)

	draw()
