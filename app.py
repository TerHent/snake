import pygame

#pygame setup

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
scr_width = 800
scr_height = 600

pygame.init()
screen = pygame.display.set_mode((scr_height,scr_width))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass

    clock.tick(144)
