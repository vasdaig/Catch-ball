
import pygame
import random
import sys
from conf import *
from main_menu import MainMenu

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ловец шаров")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Звуки
catch_sound = pygame.mixer.Sound("yes.mp3")
miss_sound = pygame.mixer.Sound("no.mp3")
gameover_sound = pygame.mixer.Sound("game_over.mp3")

def run_game():
    # Инициализация переменных
    platform_x = (WIDTH - platform_width) // 2
    platform_y = HEIGHT - platform_height - 10
    balls = []
    score = 0
    missed = 0
    max_missed = 5
    game_over = False

    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 1000)

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            elif event.type == SPAWN_EVENT and not game_over:
                x = random.randint(ball_radius, WIDTH - ball_radius)
                balls.append([x, 0])

        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[pygame.K_LEFT] and platform_x > 0:
                platform_x -= platform_speed
            if keys[pygame.K_RIGHT] and platform_x < WIDTH - platform_width:
                platform_x += platform_speed

        if not game_over:
            for ball in balls[:]:
                ball[1] += ball_speed

                if (platform_y <= ball[1] + ball_radius <= platform_y + platform_height and
                    platform_x <= ball[0] <= platform_x + platform_width):
                    balls.remove(ball)
                    score += 1
                    catch_sound.play()
                elif ball[1] > HEIGHT:
                    balls.remove(ball)
                    missed += 1
                    miss_sound.play()
                    if missed >= max_missed:
                        game_over = True
                        gameover_sound.play()

        # Отрисовка
        for ball in balls:
            pygame.draw.circle(screen, RED, (ball[0], ball[1]), ball_radius)

        pygame.draw.rect(screen, BLACK, (platform_x, platform_y, platform_width, platform_height))

        score_text = font.render(f"Счет: {score}  Промахи: {missed}/{max_missed}", True, BLACK)
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = font.render("Игра окончена. Нажмите Esc для меню.", True, (200, 0, 0))
            screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2))
            if keys[pygame.K_ESCAPE]:
                return "menu"

        pygame.display.flip()
        clock.tick(FPS)

def main():
    menu = MainMenu(screen, font)

    while True:
        choice = menu.run()
        if choice == "start":
            result = run_game()
            if result == "exit":
                break
        elif choice == "exit":
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

