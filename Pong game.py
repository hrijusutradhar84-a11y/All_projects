import pygame
import sys
import random
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG GAME")

PADDLE_WIDTH, PADDLE_HEIGHT = 15, 120
BALL_SIZE = 15

player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
Auto_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

player_speed = 7

ball_speed_x = 6
ball_speed_y = 6
Auto_speed = random.randint(5, 6)
player_score = 0
Auto_score = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= player_speed
    if keys[pygame.K_s] and player_paddle.bottom < HEIGHT:
        player_paddle.y += player_speed

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player_paddle):
        ball_speed_x = abs(ball_speed_x)  # Ensure the ball moves to the right
    if ball.colliderect(Auto_paddle):
        ball_speed_x = -abs(ball_speed_x)  # Ensure the ball moves to the left
        Auto_speed = random.randint(5, 6)

    # Move the Auto paddle
    if Auto_paddle.centery < ball.centery and Auto_paddle.bottom < HEIGHT:
        Auto_paddle.y += Auto_speed
    elif Auto_paddle.centery > ball.centery and Auto_paddle.top > 0:
        Auto_paddle.y -= Auto_speed

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the paddles and the ball
    pygame.draw.rect(screen, (255, 255, 255), player_paddle)
    pygame.draw.rect(screen, (255, 255, 255), Auto_paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    if ball.x < 0:
        Auto_score += 1  # Auto scores when ball goes past left wall
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x = 6  # Reset back to full speed!
        ball_speed_y = random.choice([-6, 6]) # Bonus: randomize vertical direction!

    elif ball.x > WIDTH:
        player_score += 1  # Player scores when ball goes past right wall
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x = -6  # Send it back to the Auto paddle at full speed!
        ball_speed_y = random.choice([-6, 6])

    # Update the display
    pygame.display.flip()
    clock.tick(60)