import pygame
from colors import COLORS

pygame.init()
pygame.font.init()

class Screen:
    def __init__(self, width=640, height=400):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.cursor = (0, 0)
        self.text_background = (0, 0, 0)  # Default to BLACK
        self.text_color = (255, 255, 255)  # Default to WHITE
        self.font = pygame.font.Font("PerfectDOSVGA437.ttf", 15)
        self.monochrome_mode = False
        self.color_iter = iter(COLORS)

        
    def GotoXY(self, x, y):
        if x not in range(1, 81) or y not in range(1, 26):
            raise ValueError("GotoXY out of bounds.")
        cursor_x = (x * 8) - 8
        cursor_y = (y * 16) - 16
        self.cursor = (cursor_x, cursor_y)

    def Write(self, text):
        txt = self.font.render(text, False, self.text_color)
        txt_background = len(text) * 8
        pygame.draw.rect(self.window, self.text_background, (self.cursor[0], self.cursor[1], txt_background, 16))
        self.window.blit(txt, self.cursor)
        pygame.display.flip()

    
    def Writeln(self, text):
        txt = self.font.render(text, False, self.text_color)
        txt_background = len(text) * 8
        pygame.draw.rect(self.window, self.text_background, (self.cursor[0], self.cursor[1], txt_background, 16))
        self.window.blit(txt, self.cursor)

        cursor_x, cursor_y = self.cursor
        cursor_y += 16 
        if cursor_y >= self.WINDOW_HEIGHT:
            cursor_y = 0 
        self.cursor = (cursor_x, cursor_y)
        pygame.display.flip()

    def ClearScreen(self):
        self.window.fill(COLORS[0])
        self.cursor = (0, 0)
        pygame.display.update() 
    
    def TextColor(self, color_index):
        self.text_color = COLORS[color_index]

    def TextBackground(self, color_index):
        self.text_background = COLORS[color_index]

    def setMonochrome(self, boolean):
        self.monochrome_mode = boolean
    
    def Col(self, num1, num2):
        if self.monochrome_mode == False:
            self.TextColor(num1)
        else:
            self.TextColor(num2)
    
    def Bak(self, num1, num2):
        if self.monochrome_mode == False:
            self.TextBackground(num1)
        else:
            self.TextBackground(num2)
    
    def Flash(self, x, y, text):
        x = (x * 8) - 8
        y = (x * 16) - 16
        #global color_iter
        flashing = True
    
        while flashing:
            try:
                value = next(self.color_iter)
            except StopIteration:
                self.color_iter = iter(COLORS)
                value = next(self.color_iter)
    
            txt = self.font.render(text, False, value)
            self.window.blit(txt, (x, y))
    
            pygame.time.delay(20)
            pygame.display.flip()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    flashing = False
