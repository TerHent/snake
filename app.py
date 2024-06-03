import pygame
import random

# Game setup
block = 10
scr_width = 800
scr_height = 600

pygame.init()
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont('Arial', 35)

# Food setup
food_pos = [random.randrange(1, (scr_width//block)) * block, random.randrange(1, (scr_height//block)) * block]
food_spawn = True

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)

# Initialize score
score = 0
def show_score():
    score_text = font.render(f'Score: {score}', True, black)
    screen.blit(score_text, [10, 10])

# Snake setup
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

# Function to generate new food position
def generate_food():
    return [random.randrange(1, (scr_width // block)) * block, random.randrange(1, (scr_height // block)) * block]

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'

    # Update direction
    direction = change_to

    # Update snake position based on direction
    if direction == 'RIGHT':
        snake_pos[0] += block
    if direction == 'LEFT':
        snake_pos[0] -= block
    if direction == 'UP':
        snake_pos[1] -= block
    if direction == 'DOWN':
        snake_pos[1] += block

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 10  # Increase score
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = generate_food()
    food_spawn = True

    # Check for collision with boundaries or itself
    if snake_pos[0] < 0 or snake_pos[0] >= scr_width or snake_pos[1] < 0 or snake_pos[1] >= scr_height:
        running = False
    for segment in snake_body[1:]:
        if snake_pos == segment:
            running = False

    # Rendering
    screen.fill(white)
    for segment in snake_body:
        pygame.draw.rect(screen, green, [segment[0], segment[1], block, block])
    pygame.draw.rect(screen, red, [food_pos[0], food_pos[1], block, block])
    show_score()
    pygame.display.flip()

    clock.tick(20)  # Adjust the speed of the game

pygame.quit()
