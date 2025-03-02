import pygame

pygame.init()
pygame.font.init()

class Screen:
    def __init__(self, width=640, height=400):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.cursor = (0, 0)
        self.text_background = (170, 0, 0)  # Default to RED
        self.text_color = (170, 0, 0)  # Default to RED
        self.font = pygame.font.Font("PerfectDOSVGA437.ttf", 15)

    def goto_xy(self, x, y):
        if x not in range(0, 80) or y not in range(0, 25):
            raise ValueError("GotoXY out of bounds.")
        cursor_x = x * 8
        cursor_y = y * 16
        self.cursor = (cursor_x, cursor_y)

    def write(self, text):
        txt = self.font.render(text, False, self.text_color)
        txt_background = len(text) * 8
        pygame.draw.rect(self.window, self.text_background, (self.cursor[0], self.cursor[1], txt_background, 16))
        self.window.blit(txt, self.cursor)

        # Replication of writeln
        cursor_x, cursor_y = self.cursor
        cursor_y += 16 
        if cursor_y >= self.WINDOW_HEIGHT:
            cursor_y = 0 
        self.cursor = (cursor_x, cursor_y)
    
    def set_text_background(self, color):
        self.text_background = color

    def set_text_color(self, color):
        self.text_color = color

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 170)
GREEN = (0, 170, 0)
CYAN = (0, 170, 170)
RED = (170, 0, 0)
MAGENTA = (170, 0, 170)
BROWN = (170, 85, 0)
LIGHT_GRAY = (170, 170, 170)
DARK_GRAY = (85, 85, 85)
LIGHT_BLUE = (85, 85, 255)
LIGHT_GREEN = (85, 255, 85)
LIGHT_CYAN = (85, 255, 255)
LIGHT_RED = (255, 85, 85)
LIGHT_MAGENTA = (255, 85, 255)
YELLOW = (255, 255, 85)
WHITE = (255, 255, 255)