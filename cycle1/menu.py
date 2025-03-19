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
    screen.Col(9,9)  
    screen.Bak(0,0)   
    screen.GotoXY(31, 2)
    screen.Write("KINGDOM OF KROZ 2")

    screen.Col(15, 15)
    screen.GotoXY(18, 10)
    screen.Write("Is your screen Color or Monochrome (C/M)? ") 
    
    pygame.display.update()
    
    # Input stuff
    inputReceived = False
    blink = True
    systemColor = None
    while not inputReceived:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key in ('c', 'C'):
                    systemColor = "color"
                    inputReceived = True
                elif key in ('m', 'M'):
                    systemColor = "monochrome"
                    inputReceived = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Blink cursor
        screen.GotoXY(60, 10)
        if blink:
            screen.Write("C")
        else:
            screen.Write(" ")
        pygame.display.update()
        pygame.time.delay(500)
        blink = not blink

    # Informs user of color choice (variable systemColor) before proceeding to next screen
    screen.GotoXY(60, 10)
    screen.Write("C" if systemColor == "color" else "M")
    pygame.display.update()
    pygame.time.delay(100)

    screen.ClearScreen()
    return systemColor

# Speed menu
def speedScreen():
    screen.Col(9,9)  
    screen.Bak(0,0)   
    screen.GotoXY(31, 2)
    screen.Write("KINGDOM OF KROZ 2")
    
    screen.Col(15,15)
    screen.GotoXY(28, 14)
    screen.Write("Slow or Fast PC (S/F)? ") 
    
    screen.TextColor(7)
    screen.GotoXY(9, 17)
    screen.Write("If you have an older PC (like an XT model) choose 'S' for Slow.") 
    
    screen.GotoXY(10, 19)
    screen.Write("If you have a PC AT, 80386 chip, etc., choose "F" for Fast.") 
    
    screen.GotoXY(32, 21)
    screen.Write("(Default = Slow)")
    
    pygame.display.update()
    
    # Input stuff
    inputReceived = False
    blink = True
    systemColor = None
    while not inputReceived:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key in ('s', 'S'):
                    systemSpeed = "slow"
                    inputReceived = True
                elif key in ('f', 'F'):
                    systemSpeed = "fast"
                    inputReceived = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Blink cursor
        screen.Col(15,15)
        screen.Bak(0,0)
        screen.GotoXY(51, 14)
        if blink:
            screen.Write("S")
        else:
            screen.Write(" ")
        pygame.display.update()
        pygame.time.delay(500)
        blink = not blink

    # Informs user of color choice (variable systemSpeed) before proceeding to next screen
    screen.GotoXY(51, 14)
    screen.Write("S" if systemSpeed == "slow" else "F")
    pygame.display.update()
    pygame.time.delay(100)

    screen.ClearScreen()
    return systemSpeed

# Logo screen
def logoScreen():
    screen.Col(15,15)
    screen.Bak(0,0)
    screen.GotoXY(28,2)
    screen.Write('Apogee Software Presents')
    
    screen.Col(14,15)
    screen.GotoXY(10, 19)    
    screen.Write("KINGDOM OF KROZ II -- UPDATED VOLUME THREE OF THE KROZ SERIES")

    screen.GotoXY(24, 21)
    screen.Write("Copyright (C) 1990 Scott Miller")
    
    screen.GotoXY(12, 23)
    screen.Write("User-Supported Software -- $7.50 Registration Fee Requi4")

    screen.Col(11,7)
    screen.GotoXY(27,24)
    screen.Write("Press any key to continue.")
    
    # logo and rainobow
    rainbow = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    colorIndex = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                running = False

        screen.TextColor(rainbow[colorIndex])
        screen.Bak(0,0)
        screen.GotoXY(1, 5)
        screen.Writeln('     ÛÛÛ     ÛÛÛ     ÛÛÛÛÛÛÛÛÛÛ         ÛÛÛÛÛÛÛÛÛÛÛ        ÛÛÛÛÛÛÛÛÛÛÛÛÛ  (R)')
        screen.Writeln('     ÛÛÛ±±  ÛÛÛ±±±   ÛÛÛ±±±±±ÛÛÛ±      ÛÛÛ±±±±±±±ÛÛÛ±        ±±±±±±ÛÛÛÛ±±±')
        screen.Writeln('     ÛÛÛ±± ÛÛÛ±±±    ÛÛÛ±±   ÛÛÛ±±     ÛÛÛ±±     ÛÛÛ±±            ÛÛÛ±±±±')
        screen.Writeln('     ÛÛÛ±±ÛÛÛ±±±     ÛÛÛ±±   ÛÛÛ±±    ÛÛÛ±±±      ÛÛÛ±           ÛÛÛ±±±')
        screen.Writeln('     ÛÛÛ±ÛÛÛ±±±      ÛÛÛÛÛÛÛÛÛÛ±±±    ÛÛÛ±±       ÛÛÛ±±         ÛÛÛ±±±')
        screen.Writeln('     ÛÛÛÛÛÛ±±±       ÛÛÛ±±ÛÛÛ±±±±     ÛÛÛ±±       ÛÛÛ±±        ÛÛÛ±±±')
        screen.Writeln('     ÛÛÛ±ÛÛÛ±        ÛÛÛ±± ÛÛÛ±        ÛÛÛ±      ÛÛÛ±±±       ÛÛÛ±±±')
        screen.Writeln('     ÛÛÛ±±ÛÛÛ±       ÛÛÛ±±  ÛÛÛ±       ÛÛÛ±±     ÛÛÛ±±      ÛÛÛÛ±±±')
        screen.Writeln('     ÛÛÛ±± ÛÛÛ±      ÛÛÛ±±   ÛÛÛ±       ÛÛÛÛÛÛÛÛÛÛÛ±±±     ÛÛÛÛÛÛÛÛÛÛÛÛÛ')
        screen.Writeln('     ÛÛÛ±±  ÛÛÛ±       ±±±     ±±±        ±±±±±±±±±±±        ±±±±±±±±±±±±±')
        screen.Writeln('     ÛÛÛ±±   ÛÛÛ±')
        screen.Writeln('     ÛÛÛ±±    ÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛ')
        screen.Writeln('       ±±±      ±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±')

        pygame.display.update()
        pygame.time.delay(300)

        colorIndex = (colorIndex + 1) % len(rainbow)

    screen.ClearScreen()

# Difficulty Screen
def difficultyScreen():
    window.fill(COLORS[1])

    screen.Bak(4,7)
    screen.GotoXY(30,1)
    screen.Write("ÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜÜ")
    
    screen.GotoXY(30,3)
    screen.Write("ßßßßßßßßßßßßßßßßßßßß")

    screen.Col(15,15)
    screen.Bak(1,0)
    screen.GotoXY(25, 5)
    screen.Write("An Apogee Software Production")
    
    screen.GotoXY(28, 7)
    screen.Write("Created by Scott Miller")
    
    screen.GotoXY(1, 9)
    screen.Col(11,7)
    screen.Writeln('  Kingdom of Kroz is a game of adventure, exploration and survival.   You are')
    screen.Writeln('  a fearless archaeologist in search of the Magical Amulet,  hidden somewhere')
    screen.Writeln('  deep in the vast and dangerous underground kingdom.   You enter the kingdom')
    screen.Writeln('  through a secret tunnel and ignite your brass lantern. Your only protection')
    screen.Writeln('  is a worn leather whip and your ingenuity.  Sweat beading on your forehead,')
    screen.Writeln('                you embark on a journey that may be your last...')
    
    screen.Col(10,7)
    screen.GotoXY(1,17)    
    screen.Write('         Use the cursor keys to move yourself (') 
    screen.GotoXY(48,17)
    screen.Col(14,15)
    screen.Write('')
    screen.GotoXY(49,17)
    screen.Col(10, 17)
    screen.Write(') through the kingdom.')
    
    screen.GotoXY(1,18)
    screen.Writeln('            Use your whip (press W) to destroy all nearby creatures.');
    screen.Writeln('       You are on your own to discover what other mysteries await--some');
    screen.Writeln('                           helpful, others deadly...');
    
    screen.GotoXY(13,22)
    screen.Col(14,7)
    screen.Write('Are you a ')
    screen.Col(15,15)
    screen.GotoXY(23,22)
    screen.Write('N')
    screen.GotoXY(24,22)
    screen.Col(14,7)
    screen.Write('ovice, an ')
    screen.GotoXY(34,22)
    screen.Col(15,15)
    screen.Write('E')
    screen.Col(14,7)
    screen.GotoXY(35,22)
    screen.Write('xperienced or an ')
    screen.GotoXY(52,22)
    screen.Col(15,15)
    screen.Write('A')
    screen.Col(14,7)
    screen.GotoXY(53,22)
    screen.Write('dvanced player?')

    #flashing and input handling
    rainbow = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    colorIndex = 0
    inputReceived = False
    blink = True
    difficulty = None
    inputBlinkTimer = pygame.time.get_ticks()
    rainbowBlinkTime = pygame.time.get_ticks()

    screen.TextColor(rainbow[colorIndex])
    screen.Bak(4,7)
    screen.GotoXY(30, 2)
    screen.Write(' KINGDOM OF KROZ II ')
    pygame.display.update()

    while not inputReceived:
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key in ('n', 'N'):
                    screen.Bak(1,0)  
                    screen.GotoXY(13,22)
                    screen.Write("                                                         ")
                    screen.GotoXY(35,22)  
                    screen.Col(14,7)
                    screen.Bak(1,0)
                    screen.Write("Novice")
                    screen.GotoXY(27,24)
                    screen.Col(8,7)
                    screen.Write("Press any key to continue.")
                    difficulty = "novice"
                    inputReceived = True
                elif key in ('e', 'E'):
                    screen.Bak(1,0)  
                    screen.GotoXY(13,22)
                    screen.Write("                                                         ")
                    screen.GotoXY(32,22)  
                    screen.Col(14,7)
                    screen.Bak(1,0)
                    screen.Write("Experienced")
                    screen.GotoXY(27,24)
                    screen.Col(8,7)
                    screen.Write("Press any key to continue.")
                    difficulty = "experienced"
                    inputReceived = True
                elif key in ('a', 'A'):
                    screen.Bak(1,0)  
                    screen.GotoXY(13,22)
                    screen.Write("                                                         ")
                    screen.GotoXY(34,22)  
                    screen.Col(14,7)
                    screen.Bak(1,0)
                    screen.Write("Advanced")
                    screen.GotoXY(27,24)
                    screen.Col(8,7)
                    screen.Write("Press any key to continue.")
                    difficulty = "advanced"
                    inputReceived = True
                elif key in ('x', 'X'):
                    screen.Bak(1,0)  
                    screen.GotoXY(13,22)
                    screen.Write("                                                         ")
                    screen.GotoXY(35,22)  
                    screen.Col(14,7)
                    screen.Bak(1,0)
                    screen.Write("Secret")
                    screen.GotoXY(27,24)
                    screen.Col(8,7)
                    screen.Write("Press any key to continue.")
                    difficulty = "secret"
                    inputReceived = True

        # Update rainbow title
        if current_time - rainbowBlinkTime >= 300:
            screen.TextColor(rainbow[colorIndex])
            screen.Bak(4,7)
            screen.GotoXY(30, 2)
            screen.Write(' KINGDOM OF KROZ II ')
            colorIndex = (colorIndex + 1) % len(rainbow)
            rainbowBlinkTime = current_time

        # Blink "N" before selection
        if not inputReceived:
            if current_time - inputBlinkTimer >= 500:
                screen.GotoXY(68, 22)
                screen.Col(14,7)
                if blink:
                    screen.Write("N")
                else:
                    screen.Write(" ")
                blink = not blink
                inputBlinkTimer = current_time

        pygame.display.update()

    waiting = True
    difficultyBlinkTimer = pygame.time.get_ticks()
    difficultyBlink = True
    while waiting:
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

        # Rainbow blinker (in selection of difficulty)
        if current_time - rainbowBlinkTime >= 300:
            screen.TextColor(rainbow[colorIndex])
            screen.Bak(4,7)
            screen.GotoXY(30, 2)
            screen.Write(' KINGDOM OF KROZ II ')
            colorIndex = (colorIndex + 1) % len(rainbow)
            rainbowBlinkTime = current_time

        # Difficulty blinker
        if current_time - difficultyBlinkTimer >= 500:
            screen.Bak(1,0)
            screen.GotoXY(13,22)
            screen.Write("                                                         ")
            screen.GotoXY(35,22)
            screen.Col(14,7)
            if difficultyBlink:
                if difficulty == "novice":
                    screen.GotoXY(35,22)
                    screen.Write("Novice")
                elif difficulty == "experienced":
                    screen.GotoXY(32,22)
                    screen.Write("Experienced")
                elif difficulty == "advanced":
                    screen.GotoXY(34,22)
                    screen.Write("Advanced")
                elif difficulty == "secret":
                    screen.GotoXY(35,22)
                    screen.Write("Secret")
            pygame.display.update()
            difficultyBlink = not difficultyBlink
            difficultyBlinkTimer = current_time

    screen.ClearScreen()
    return difficulty

# Registration screen
def registrationScreen():
    window.fill(COLORS[1])

    screen.Col(15,15)
    screen.Bak(1,0)
    screen.GotoXY(22,1)
    screen.Writeln('KINGDOM OF KROZ II Ä HOW TO REGISTER');
    
    screen.GotoXY(1, 2)
    screen.Write("ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ")

    screen.GotoXY(1,3)
    screen.Col(7,7)
    screen.Writeln("  This is a shareware game, meaning it's user-supported.  If you enjoy this")
    screen.Writeln("game you are asked by the author to please send a registration check in the")
    screen.Writeln("amount of $7.50 to Apogee Software.")
    screen.Writeln("  This registration fee will qualify you to order any of the other Kroz")
    screen.Writeln("volumes available:")

    screen.Writeln("")
    screen.Col(15,7)
    screen.Writeln('  þ Caverns of Kroz   - the first discovery of Kroz')
    screen.Writeln('  þ Dungeons of Kroz  - the dark side of Kroz, fast-paced action')
    screen.Writeln('  þ Kingdom of Kroz I - the national contest winner ("Best Game" in 1988)')
    screen.Writeln('  þ Return to Kroz    - the discovery of entirely new underground chambers')
    screen.Writeln('  þ Temple of Kroz    - the bizarre side of Kroz, nothing is what it seems')
    screen.Writeln('  þ The Final Crusade of Kroz - the surprising finish?');

    screen.Writeln("")
    screen.Col(7,7)
    screen.Writeln('Each game is priced $7.50 each, any three for $20, or all six for only $35.')
    screen.Writeln('You''ll also get a secret code that makes this game easier to complete,')
    screen.Writeln('plus a "Hints, Tricks and Scoring Secrets" guide and "The Domain of Kroz" map.')

    screen.Writeln("")
    screen.Writeln("Please make checks payable to:")

    screen.GotoXY(31, 20)
    screen.Col(14,7)
    screen.Writeln('   Apogee Software    (phone: 214/240-0614)')
    screen.GotoXY(31,21)
    screen.Writeln('   4206 Mayflower')
    screen.GotoXY(1,22)    
    screen.Col(15,15)
    screen.Writeln("Address always valid!")
    screen.GotoXY(31,22)
    screen.Col(14,7)
    screen.Write('   Garland, TX 75043  (USA)')

    screen.GotoXY(1,24)
    screen.Col(7,7)
    screen.Write("Thank you and enjoy the game.  -- Scott Miller")

    running = True
    blink = True
    last_blink_time = pygame.time.get_ticks()

    while running:
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                running = False

        if current_time - last_blink_time >= 300:
            screen.GotoXY(27,25)
            screen.Col(0,0)
            if blink:
                screen.Write('Press any key to continue.')
            else:
                screen.Write('                          ') 
            blink = not blink
            last_blink_time = current_time

        pygame.display.update()

#Main menu
def mainMenu():
    while True:
        screen.Bak(0,0)
        screen.ClearScreen()

        screen.Col(15,9)
        screen.GotoXY(31,2)
        screen.Write('KINGDOM OF KROZ II')
        
        screen.GotoXY(17,4)
        screen.Col(6,7)
        screen.Write('Copyright (c) 1990 Apogee Software Productions')
        
        screen.GotoXY(25,6)
        screen.Write('Version 2.0 -- by Scott Miller')
        
        screen.GotoXY(6,8)
        screen.Col(2,7)
        screen.Writeln('THIS GAME MAY BE DISTRIBUTED BY SHAREWARE OR PUBLIC DOMAIN LIBRARIES,')
        screen.GotoXY(6,9)
        screen.Writeln('OR BULLETIN BOARD SYSTEMS. NO NEED TO INQUIRE FOR WRITTEN PERMISSION.')
        
        screen.GotoXY(1,10)
        screen.Col(4,7)
        screen.Write('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
        
        #Menu options
        screen.Col(14,15)
        screen.GotoXY(28,12)
        screen.Write('B') 
        screen.GotoXY(29,12)
        screen.Col(11,7)
        screen.Write('egin your descent into Kroz...')
        
        screen.Col(14,15)
        screen.GotoXY(28,14)
        screen.Write('I')
        screen.GotoXY(29,14)
        screen.Col(11,7)
        screen.Write('nstructions')
        
        screen.Col(14,15)
        screen.GotoXY(28,16)
        screen.Write('M')
        screen.GotoXY(29,16)
        screen.Col(11,7)
        screen.Write('arketing Kroz')
        
        screen.Col(14,15)
        screen.GotoXY(28,18)
        screen.Write('S')
        screen.GotoXY(29,18)
        screen.Col(11,7)
        screen.Write('tory Behind Kroz')
        
        screen.Col(14,15)
        screen.GotoXY(28,20)
        screen.Write('O')
        screen.GotoXY(29,20)
        screen.Col(11,7)
        screen.Write('riginal Kroz Games')
        
        screen.Col(14,15)
        screen.GotoXY(28,22)
        screen.Write('A')
        screen.GotoXY(29,22)
        screen.Col(11,7)
        screen.Write('bout the Author')
        
        screen.GotoXY(26,24)
        screen.Col(15,0)
        screen.Bak(1,7)
        screen.Write('Your choice (B/I/M/S/O/A)? ')

        choice = None
        blink = True
        last_blink_time = pygame.time.get_ticks()
        
        while choice is None:
            current_time = pygame.time.get_ticks()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)
                    if key in ('b', 'B', 'i', 'I', 'm', 'M', 's', 'S', 'o', 'O', 'a', 'A'):
                        choice = key.upper()
                        screen.Write(choice)
                        pygame.display.update()
                        pygame.time.delay(100)

            # Blink default B
            if current_time - last_blink_time >= 500:
                screen.GotoXY(54,24)
                if blink:
                    screen.Write('B')
                else:
                    screen.Write(' ')
                blink = not blink
                last_blink_time = current_time

            pygame.display.update()

        screen.ClearScreen()
        
        # Handle menu choices
        if choice == 'B':
            return 'begin'  
        elif choice == 'I':
            instructionScreen()
        elif choice == 'M':
            marketingScreen()
        elif choice == 'S':
            storyScreen()
        elif choice == 'O':
            originalScreen()
        elif choice == 'A':
            aboutScreen()

def beginGame():
    screen.ClearScreen()

def instructionScreen():
    screen.ClearScreen()

def marketingScreen():
    screen.ClearScreen()

def storyScreen():  
    screen.ClearScreen()

def originalScreen():
    screen.ClearScreen()

def aboutScreen():
    screen.ClearScreen()

# Program
def main():
    
    # Calls menu screens
    systemColor = colorScreen()
    systemSpeed = speedScreen() 
    logoScreen()
    difficultyScreen()
    registrationScreen()
    if mainMenu() == "begin":
        beginGame()

    pygame.display.update()
    pygame.time.delay(2000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()