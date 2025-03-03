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

# Color menu
def colorScreen():
    screen.set_text_color(BLUE)
    screen.set_text_background(BLACK)
    screen.goto_xy(31, 2)
    screen.write("KINGDOM OF KROZ 2")
    
    screen.set_text_color(WHITE)
    screen.set_text_background(BLACK)
    screen.goto_xy(18, 10)
    screen.write("Is your screen Color or Monochrome (C/M)? ") 
    
    pygame.display.update()
    
    # Input stuff
    input_received = False
    blink = True
    systemColor = None
    while not input_received:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key in ('c', 'C'):
                    systemColor = "color"
                    input_received = True
                elif key in ('m', 'M'):
                    systemColor = "monochrome"
                    input_received = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Blink cursor
        screen.goto_xy(60, 10)
        if blink:
            screen.write("C")
        else:
            screen.write(" ")
        pygame.display.update()
        pygame.time.delay(500)
        blink = not blink

    # Informs user of color choice (variable systemColor) before proceeding to next screen
    screen.goto_xy(60, 10)
    screen.write("C" if systemColor == "color" else "M")
    pygame.display.update()
    pygame.time.delay(100)

    screen.clear_screen()
    return systemColor

# Speed menu
def speedScreen(systemSpeed):
    screen.set_text_color(BLUE)
    screen.set_text_background(BLACK)
    screen.goto_xy(31, 2)
    screen.write("KINGDOM OF KROZ 2")
    
    screen.set_text_color(WHITE)
    screen.set_text_background(BLACK)
    screen.goto_xy(28, 14)
    screen.write("Slow or Fast PC (S/F)? ") 
    
    screen.set_text_color(LIGHT_GRAY)
    screen.set_text_background(BLACK)
    screen.goto_xy(9, 17)
    screen.write("If you have an older PC (like an XT model) choose 'S' for Slow.") 
    
    screen.goto_xy(10, 19)
    screen.write("If you have a PC AT, 80386 chip, etc., choose "F" for Fast.") 
    
    screen.goto_xy(32, 21)
    screen.write("(Default = Slow)")
    
    pygame.display.update()
    
    # Input stuff
    input_received = False
    blink = True
    systemColor = None
    while not input_received:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key in ('s', 'S'):
                    systemSpeed = "slow"
                    input_received = True
                elif key in ('f', 'F'):
                    systemSpeed = "fast"
                    input_received = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Blink cursor
        screen.set_text_color(WHITE)
        screen.set_text_background(BLACK)
        screen.goto_xy(51, 14)
        if blink:
            screen.write("S")
        else:
            screen.write(" ")
        pygame.display.update()
        pygame.time.delay(500)
        blink = not blink

    # Informs user of color choice (variable systemSpeed) before proceeding to next screen
    screen.goto_xy(51, 14)
    screen.write("S" if systemSpeed == "slow" else "F")
    pygame.display.update()
    pygame.time.delay(100)

    screen.clear_screen()
    return systemSpeed

def logoScreen():
    screen.set_text_color(WHITE)
    screen.set_text_background(BLACK)
    screen.goto_xy(28,2)
    screen.write('Apogee Software Presents')
    
    screen.set_text_color(YELLOW)
    screen.set_text_background(BLACK)
    screen.goto_xy(10, 19)    
    screen.write("KINGDOM OF KROZ II -- UPDATED VOLUME THREE OF THE KROZ SERIES")

    screen.goto_xy(24, 21)
    screen.write("Copyright (C) 1990 Scott Miller")
    
    screen.goto_xy(12, 23)
    screen.write("User-Supported Software -- $7.50 Registration Fee Required")

    screen.set_text_color(LIGHT_CYAN)
    screen.goto_xy(27,24)
    screen.write("Press any key to continue.")
    
    # logo and variables
    rainbow = [BLUE, GREEN, CYAN, RED, MAGENTA, YELLOW, WHITE, BROWN, LIGHT_GRAY, DARK_GRAY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, LIGHT_MAGENTA]
    colorIndex = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                running = False

        screen.set_text_color(rainbow[colorIndex])
        screen.set_text_background(BLACK)
        screen.goto_xy(1, 5)
        screen.writeln('     ÛÛÛ     ÛÛÛ     ÛÛÛÛÛÛÛÛÛÛ         ÛÛÛÛÛÛÛÛÛÛÛ        ÛÛÛÛÛÛÛÛÛÛÛÛÛ  (R)')
        screen.writeln('     ÛÛÛ±±  ÛÛÛ±±±   ÛÛÛ±±±±±ÛÛÛ±      ÛÛÛ±±±±±±±ÛÛÛ±        ±±±±±±ÛÛÛÛ±±±')
        screen.writeln('     ÛÛÛ±± ÛÛÛ±±±    ÛÛÛ±±   ÛÛÛ±±     ÛÛÛ±±     ÛÛÛ±±            ÛÛÛ±±±±')
        screen.writeln('     ÛÛÛ±±ÛÛÛ±±±     ÛÛÛ±±   ÛÛÛ±±    ÛÛÛ±±±      ÛÛÛ±           ÛÛÛ±±±')
        screen.writeln('     ÛÛÛ±ÛÛÛ±±±      ÛÛÛÛÛÛÛÛÛÛ±±±    ÛÛÛ±±       ÛÛÛ±±         ÛÛÛ±±±')
        screen.writeln('     ÛÛÛÛÛÛ±±±       ÛÛÛ±±ÛÛÛ±±±±     ÛÛÛ±±       ÛÛÛ±±        ÛÛÛ±±±')
        screen.writeln('     ÛÛÛ±ÛÛÛ±        ÛÛÛ±± ÛÛÛ±        ÛÛÛ±      ÛÛÛ±±±       ÛÛÛ±±±')
        screen.writeln('     ÛÛÛ±±ÛÛÛ±       ÛÛÛ±±  ÛÛÛ±       ÛÛÛ±±     ÛÛÛ±±      ÛÛÛÛ±±±')
        screen.writeln('     ÛÛÛ±± ÛÛÛ±      ÛÛÛ±±   ÛÛÛ±       ÛÛÛÛÛÛÛÛÛÛÛ±±±     ÛÛÛÛÛÛÛÛÛÛÛÛÛ')
        screen.writeln('     ÛÛÛ±±  ÛÛÛ±       ±±±     ±±±        ±±±±±±±±±±±        ±±±±±±±±±±±±±')
        screen.writeln('     ÛÛÛ±±   ÛÛÛ±');       
        screen.writeln('     ÛÛÛ±±    ÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛ')
        screen.writeln('       ±±±      ±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

        pygame.display.update()
        pygame.time.delay(300)

        colorIndex = (colorIndex + 1) % len(rainbow)

def difficultyScreen():
    window.fill(BLUE)

    screen.goto_xy(30,1)
    screen.write("ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ")
    
    screen.goto_xy(30,2)
    screen.set_text_color(WHITE)
    screen.write(" KINGDOM OF KROZ II ")
    
    screen.goto_xy(30,3)
    screen.write("ßßßßßßßßßßßßßßßßßßßß")

    screen.set_text_color(WHITE)
    screen.set_text_background(BLUE)
    screen.goto_xy(25, 5)
    screen.write("An Apogee Software Production")
    
    pygame.display.update()

# Program
def main():
    
    # Calls menu screens
    systemColor = colorScreen()
    systemSpeed = speedScreen(systemColor) 
    logoScreen()
    difficultyScreen()

    pygame.display.update()
    pygame.time.delay(2000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()