import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

PILLAR_HEIGHT, PILLAR_WIDTH = random.randint(100, 600), 50
BALL_SIZE = 15

ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
pillar_lower = pygame.Rect(0, HEIGHT - PILLAR_HEIGHT, PILLAR_WIDTH, PILLAR_HEIGHT)
pillar_upper = pygame.Rect(0, 0, PILLAR_WIDTH, HEIGHT - PILLAR_HEIGHT - 200)

ball_speed_x = 0.1
ball_speed_y = 0
ball_acceleration_up = 1
ball_acceleration_down = 0.2
pillar_speed = -5
score = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        ball_speed_y -= ball_acceleration_up
    else:
        ball_speed_y += ball_acceleration_down

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    pillar_lower.x += pillar_speed 
    pillar_upper.x += pillar_speed

    if pillar_lower.right < 0:
        PILLAR_HEIGHT = random.randint(100, 600)
        pillar_lower = pygame.Rect(WIDTH, HEIGHT - PILLAR_HEIGHT, PILLAR_WIDTH, PILLAR_HEIGHT)
        pillar_upper = pygame.Rect(WIDTH, 0, PILLAR_WIDTH, HEIGHT - PILLAR_HEIGHT - 200)
        score += 1

    if ball.colliderect(pillar_lower) or ball.colliderect(pillar_upper) or ball.top <= 0 or ball.bottom >= HEIGHT:
        print("Game Over! Your score:", score)
        pygame.quit()
        sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), ball)
    pygame.draw.rect(screen, (0, 255, 0), pillar_lower)
    pygame.draw.rect(screen, (0, 255, 0), pillar_upper)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)