import pygame
import random

pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the game title
pygame.display.set_caption('Car Racing Game')

# Set the game clock
clock = pygame.time.Clock()

# Load the car image
car_img = pygame.image.load('car.png')
car_width = 50
car_height = 100

# Load the background image
background_img = pygame.image.load('background.png')
background_y = 0

# Set the game font
font = pygame.font.SysFont(None, 30)

def show_score(score):
    score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def game_over():
    over_text = font.render('Game Over!', True, (255, 255, 255))
    screen.blit(over_text, (screen_width/2 - over_text.get_width()/2, screen_height/2 - over_text.get_height()/2))

# Define the main game loop
def game_loop():
    # Initialize game variables
    car_x = screen_width/2 - car_width/2
    car_y = screen_height - car_height - 10
    car_speed = 5
    score = 0
    obstacle_width = 100
    obstacle_height = 100
    obstacle_x = random.randint(0, screen_width - obstacle_width)
    obstacle_y = -obstacle_height
    obstacle_speed = 5

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        # Move the car
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < screen_width - car_width:
            car_x += car_speed

        # Move the obstacles
        obstacle_y += obstacle_speed
        if obstacle_y > screen_height:
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            obstacle_y = -obstacle_height
            score += 1
            obstacle_speed += 1

        # Check for collision
        if car_x + car_width > obstacle_x and car_x < obstacle_x + obstacle_width and car_y < obstacle_y + obstacle_height:
            game_over()
            pygame.display.update()
            pygame.time.delay(2000)
            game_running = False

        # Draw the game objects
        screen.blit(background_img, (0, background_y))
        screen.blit(car_img, (car_x, car_y))
        pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        show_score(score)

        # Update the screen
        pygame.display.update()
        clock.tick(60)

    # Quit the game
    pygame.quit()
    quit()

# Start the game loop
game_loop()
