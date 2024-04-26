import pygame
from typing import Callable
from dataclasses import dataclass

Color = tuple[int, int, int]
WHITE   : Color = (255, 255, 255)
RED     : Color = (255,   0,   0)
GREEN   : Color = (  0, 255,   0)
BLUE    : Color = (  0,   0, 255)
BLACK   : Color = (  0,   0,   0)
CYAN    : Color = ( 50, 255, 255)
MAGENTA : Color = (255,   0, 255)
YELLOW  : Color = (255, 255,   0)
ORANGE  : Color = (255, 127,   0)

@dataclass
class Button:
    text: any
    x: int
    y: int
    width: int
    height: int
    font_size: int = 42
    font_color: Color = WHITE
    border_color: Color = WHITE

    def contains(self, x: int, y: int):
        return (
            self.x <= x and x < self.x + self.width and
            self.y <= y and y < self.y + self.height
        )

@dataclass
class Label:
    text: any
    x: int
    y: int
    font_size: int = 42
    font_color: Color = WHITE

class Menu:
    width: int
    height: int
    screen: pygame.surface.Surface
    clock: pygame.time.Clock

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def run(self, setup: Callable[[], None], draw: Callable[[], None], on_touch: Callable[[int, int], None]):
        pygame.font.init()
        pygame.display.init()
        pygame.mouse.set_visible(0)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.screen.fill(BLACK)
        if setup:
            setup()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if on_touch:
                        on_touch(*pygame.mouse.get_pos())
            if draw:
                draw()
            pygame.display.flip() # Swap front and back framebuffer
            self.clock.tick(60) # Limit fps to 60

    def draw_button(self, button: Button):
        font = pygame.font.Font(None, button.font_size)
        rendered_label = font.render(str(button.text), 1, button.font_color)
        self.screen.blit(rendered_label, (button.x, button.y))
        pygame.draw.rect(self.screen, button.border_color, (button.x - 10, button.y - 10, button.width, button.height), 3)

    def draw_label(self, label: Label):
        font = pygame.font.Font(None, font_size)
        rendered_label = font.render(str(label.text), 1, label.font_color)
        self.screen.blit(rendered_label, (label.x, label.y))
