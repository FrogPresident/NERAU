# coding: utf-8
import pygame


class Text_box:
    color_inactive = (100, 100, 200)
    color_active = (200, 200, 255)

    def __init__(self, x, y):
        self.font = pygame.font.Font(None, 32)
        self.input_box = pygame.Rect(100, 100, 140, 32)
        self.input_box.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        color = (100, 100, 200)
        text = ""
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.input_box.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                color = Text_box.color_active if action else Text_box.color_inactive
                print(color)
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        text_surface = self.font.render(text, True, color)
        input_box_width = max(200, text_surface.get_width() + 10)
        self.input_box.w = input_box_width
        # show the text_box
        surface.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))
        pygame.draw.rect(surface, color, self.input_box, 3)

        return action


def main():
    # Settings
    width = 600
    height = 300
    active = False
    running = True

    # Init
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Input Box Demo")
    screen = pygame.display.set_mode((width, height))

    # Run
    speed_text_box = Text_box(300, 150)
    while running:
        speed_text_box.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Updates
        pygame.display.flip()


if __name__ == "__main__":
    main()
