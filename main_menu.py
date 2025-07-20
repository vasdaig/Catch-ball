import pygame

class MainMenu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font 
        self.options = ["Start game", "Exit"]
        self.selected_index = 0

    def draw(self):
        self.screen.fill((255, 255, 255))
        title = self.font.render("Ball ceeper", True, (0, 0, 0))
        self.screen.blit(title, (self.screen.get_width() // 2 - title.get_width() // 2, 100))

        for i, option in enumerate(self.options):
            color = (255, 0, 0) if i == self.selected_index else (0, 0, 0)
            text = self.font.render(option, True, color)
            x = self.screen.get_width() // 2 - text.get_width() // 2

            y = 200 + i * 50
            self.screen.blit(text, (x,y))

        pygame.display.flip()

    def run(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        return "start" if self.selected_index == 0 else "exit"