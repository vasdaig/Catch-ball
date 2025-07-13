import pygame
import random
import sys

from conf import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Ловец шаров")


clock = pygame.time.Clock()


running = True

platform_x = (WIDTH - platform_width) // 2
platform_y = HEIGHT - platform_height - 10

SPAWN_EVENT = pygame.USEREVENT + 1    # levels
pygame.time.set_timer(SPAWN_EVENT, 1000)     # 1000 ms

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_EVENT:
            x = random.randint(ball_radius, WIDTH - ball_radius)
            balls.append([x, 0])
    
    for ball in balls:
        ball[1] += ball_speed

    for ball in balls:
        pygame.draw.circle(screen, RED, (ball[0], ball[1]), ball_radius)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_x > 0:
        platform_x -= platform_speed

    if keys[pygame.K_RIGHT] and platform_x < WIDTH - platform_width:
        platform_x += platform_speed

    pygame.draw.rect(screen, BLACK, (platform_x, platform_y, platform_width, platform_height))

    pygame.display.flip()
    clock.tick(FPS)    

pygame.quit() 
sys.exit()