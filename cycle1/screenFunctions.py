"""Caleb Functions"""
import pygame

pygame.display.init()
pygame.font.init()

class Screen:
    def __init__(self, width=640, height=400):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.cursor = (0, 0)
        self.text_background = (170, 0, 0) 
        self.text_color = (170, 0, 0)  
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

    def set_text_background(self, color):
        self.text_background = color

    def set_text_color(self, color):
        self.text_color = color

    def clear_screen(self):
        self.window.fill((0, 0, 0))
    
    def referesh(self):
        pygame.display.update()
