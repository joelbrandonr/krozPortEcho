import pygame
import os
import time
import sys
import random
from screenFunctions import Screen
from colors import *


pygame.init()
pygame.font.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("KINGDOM OF KROZ 2")
screen = Screen()

# Menu functions
def draw_menu():
    screen.set_text_color(BLUE)
    screen.goto_xy(31, 2)
    screen.write("KINGDOM OF KROZ 2")
    
    pygame.display.update()

# Program
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        draw_menu()
        pygame.time.delay(100)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()