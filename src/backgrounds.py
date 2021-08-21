'''
**File is to be ignored**
This is the file in which I was testing out 
The changing backgrounds

'''

import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 350
screen_height = 600


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')

#define colours
bg = (255, 255, 255)

def draw_bg():
	screen.fill(bg)


run = True
while run:

	clock.tick(fps)

	#draw background
	draw_bg()

	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()