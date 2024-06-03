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
font = pygame.font.SysFont('Arial', 20)

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

def game_over():
    over_font = pygame.font.SysFont('Arial', 30)
    over_text = over_font.render('You Lose! Press R to Restart or Q to Quit', True, red)
    screen.fill(white)
    screen.blit(over_text, [scr_width // 8, scr_height // 3])
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

def reset_game():
    global snake_pos, snake_body, direction, change_to, food_pos, food_spawn, score
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    change_to = direction
    food_pos = [random.randrange(1, (scr_width // block)) * block, random.randrange(1, (scr_height // block)) * block]
    food_spawn = True
    score = 0

# Snake setup
reset_game()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
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
        food_pos = [random.randrange(1, (scr_width // block)) * block, random.randrange(1, (scr_height // block)) * block]
    food_spawn = True

    # Check for collision with boundaries or itself
    if snake_pos[0] < 0 or snake_pos[0] >= scr_width or snake_pos[1] < 0 or snake_pos[1] >= scr_height:
        if game_over():
            reset_game()
        else:
            running = False
    for segment in snake_body[1:]:
        if snake_pos == segment:
            if game_over():
                reset_game()
            else:
                running = False

    # Rendering
    screen.fill(white)
    for segment in snake_body:
        pygame.draw.rect(screen, green, [segment[0], segment[1], block, block])
    pygame.draw.rect(screen, red, [food_pos[0], food_pos[1], block, block])
    show_score()
    pygame.display.flip()

    clock.tick(20)  # Adjust the speed of the game
