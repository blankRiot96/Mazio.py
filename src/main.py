import pygame
from pygame.locals import *
import math

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 600


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mazio')

tile_size = 50

# Images
player_img = pygame.image.load('maze_player.png')
#player_img = pygame.transform.rotate(player_img, -45)
player = pygame.transform.scale(player_img, (tile_size+10, tile_size+10))
player_rect = player.get_rect(center=(300, 300))


class World():
    def __init__(self, data):
        self.tile_list = []
        # Load Images
        strong_block = pygame.image.load("strong.png")
        weak_block = pygame.image.load("weak.png")

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(strong_block, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(weak_block, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


world_data = [
    [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 1],
    [0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 2, 1, 2, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 2, 1, 2, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 2, 1, 2, 1, 2, 1, 0, 0]
]


def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = player_rect = player.get_rect(center=(300, 300))

    return rotated_surface, rotated_rect

# Define colours
bg = (25, 25, 25)

world = World(world_data)

angle = 0
idle = True

dx = 0
dy = 0

flag = False

count = 0
player_rotated_rect = player_rect = player.get_rect(center=(300, 300))
d2r = math.pi/180.0    # multiplier to easily convert degrees to radians
run = True
while run:
    clock.tick(fps)
    count += 1
    # Draw background
    screen.fill(bg)
    # Player
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        # if count % 7.5 == 0:
        #     idle = False
        #     world_data.insert(0, [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
        #     world_data.pop()
        idle = False
        speed = 2
        angle_rad = angle*d2r                           # multiply angle by math.pi/180 if it is in degrees
        dx, dy = math.cos(angle_rad), math.sin(angle_rad)   
        player_rotated_rect[0] += dx*speed
        player_rotated_rect[1] += dy*speed
    
    if key[pygame.K_DOWN]:
        pass
        # if count % 7.5 == 0:
        #     idle = False
        #     world_data.pop(0)
        #     world_data.insert(11, [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])
        idle = False
        speed = 2
        angle_rad = angle*d2r                           # multiply angle by math.pi/180 if it is in degrees
        dx, dy = math.cos(angle_rad), math.sin(angle_rad)   
        player_rotated_rect[0] -= dx*speed
        player_rotated_rect[1] -= dy*speed

    if key[pygame.K_LEFT]:
        idle = False
        angle += 1.4
    else:
        idle = True

    if key[pygame.K_RIGHT]:
        idle = False
        angle -= 1.4
    else:
        idle = True
    
    old_player_rotated_rect_center = player_rotated_rect.center 
    player_rotated = pygame.transform.rotozoom(player, angle, 1)
    player_rotated_rect.size = player_rotated.get_size()
    player_rotated_rect.center = old_player_rotated_rect_center

    if idle:
        x = player_rotated_rect[0]
        y = player_rotated_rect[1]

        if dy <= 15 and flag == False:
            dy += 0.4
        else:
            flag = True
        
        if flag:
            if dy >= 1:
                dy -= 0.4
            else: 
                flag = False
        y += dy 

        screen.blit(player_rotated, (x, y))
    else:
        screen.blit(player_rotated, player_rotated_rect)

    world = World(world_data)
    world.draw()


    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

