import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size w x l
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Snake')

# Set the colors r g b
white = (255,255,255)
gold = (255, 214.9, 0)

# Set the snake's starting position and size
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set the initial direction
direction = 'RIGHT'
change_to = direction

# Set the initial score
score = 0

# Set the initial speed
speed = 10

# Set the initial apple position
apple_position = [random.randrange(1, (window_size[0] // 10)) * 10, random.randrange(1, (window_size[1] // 10)) * 10]
apple_spawn = True

# Set the game over flag
game_over = False

# Set the clock
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
            game_over = True

    # Validate the direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update the snake position
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

   # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        apple_spawn = False
        score += 1
    else:
        snake_body.pop()

    if not apple_spawn:
        apple_position = [random.randrange(1, (window_size[0] // 10)) * 10, random.randrange(1, (window_size[1] // 10)) * 10]
        apple_spawn = True
        
    # Check if the snake has collided with the boundaries instantly
    if snake_position[0] < 0 or snake_position[0] > window_size[0]:
        game_over = True
    if snake_position[1] < 0 or snake_position[1] > window_size[1]:
        game_over = True

    # Check if the snake has collided with its own body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True

    # Fill the screen with white
    screen.fill(white)

    # Draw the snake
    for position in snake_body:
        pygame.draw.rect(screen, gold, pygame.Rect(position[0], position[1], 10, 10))

    # Draw the apple
    pygame.draw.rect(screen, gold, pygame.Rect(apple_position[0], apple_position[1], 10, 10))

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    clock.tick(speed)

# Print the final score
print("Your final score was: ", score)

# Quit Pygame
pygame.quit()

# Quit the program
quit()

    