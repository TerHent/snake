import pygame

# Game setup
block = 10
scr_width = 800
scr_height = 600

pygame.init()
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
running = True

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)


# Snake setup
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'

    # Update snake position based on direction
    if direction == 'RIGHT':
        snake_pos[0] += block
    if direction == 'LEFT':
        snake_pos[0] -= block
    if direction == 'UP':
        snake_pos[1] -= block
    if direction == 'DOWN':
        snake_pos[1] += block

    # Check for collision
    if snake_pos[0] < 0 or snake_pos[0] >= scr_width or snake_pos[1] < 0 or snake_pos[1] >= scr_height:
        running = False
    for segment in snake_body[1:]:
        if snake_pos == segment:
            running = False

    # Rendering
    screen.fill(white)
    for segment in snake_body:
        pygame.draw.rect(screen, black, [segment[0], segment[1], block, block])
    pygame.display.flip()

    clock.tick(10)
