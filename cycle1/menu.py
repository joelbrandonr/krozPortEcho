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
    screen.Col(10, 7)
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

#Starts game
def beginGame():
    screen.ClearScreen()

#Instructions Screens
def instructionScreen():
    #Screen1
    window.fill(COLORS[1])
    screen.Bak(1,0)
    screen.GotoXY(32,2)
    screen.Col(14,7)
    screen.Writeln('THE INSTRUCTIONS')

    screen.GotoXY(32,3)
    screen.Writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')

    screen.GotoXY(1,5)
    screen.Col(15,7)
    screen.Writeln('   Kingdom of Kroz is a game of exploration and survival.  Your journey will')
    screen.Writeln(' take you through 25 very dangerous chambers, each riddled with diabolical')
    screen.Writeln(' traps and hideous creatures.   Hidden in the deepest chamber lies a hidden')
    screen.Writeln(' treasure of immense value. Use the cursor pad to move 8 directions.')
    screen.Writeln('   The chambers contain dozens of treasures, spells, traps and other unknowns.')
    screen.Writeln(' Touching an object for the first time will reveal a little of its identity,')
    screen.Writeln(' but it will be left to you to decide how best to use it--or avoid it.')
    screen.Writeln('   When a creature touches you it will vanish, taking with it a few of your')
    screen.Writeln(' gems that you have collected. If you have no gems then the creature will')
    screen.Writeln(' instead take your life!  Whips can be used to kill nearby creatures, but')
    screen.Writeln(' they''re better used to smash through "breakable walls" and other terrain.')
    screen.Writeln('   Laptop and PCjr players can')
    screen.Writeln(' use the alternate cursor             U I O      ( NW N NE )')
    screen.Writeln(' pad instead of the cursor             J K       (   W E   )')
    screen.Writeln(' keys to move your man, plus          N M ,      ( SW S SE )')
    screen.Writeln(' the four normal cursor keys.')
    screen.Writeln('   It''s a good idea to save your game at every new level, therefore, if you die')
    screen.Writeln(' you can easily restore the game at that level and try again.')
    screen.Writeln('   Registered users will get a "secret code" that makes this game much easier!')
    screen.Flash(27,25,'Press any key to continue.')

    #Screen 2
    screen.ClearScreen()
    window.fill(COLORS[1])
    screen.Bak(1,0)
    screen.GotoXY(32,2)
    screen.Col(14,7)
    screen.Writeln('THE INSTRUCTIONS')

    screen.GotoXY(32,3)
    screen.Writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')

    screen.GotoXY(1,5)
    screen.Col(15,7)
    screen.Writeln('   Kingdom of Kroz will present you with many challenges. You will venture deep')
    screen.Writeln(' underground and probably not make it out alive!')
    screen.Writeln
    screen.Writeln(' Hints:  þ Don''t forget to use the Home, End, PgUp, and PgDn keys to move your')
    screen.Writeln('           on-screen character diagonally (along with the marked cursor keys).')
    screen.Writeln('         þ Use your player to touch each new object to find out about it.  When')
    screen.Writeln('           you first touch an object a message appears at the bottom of the')
    screen.Writeln('           screen that describes it.')
    screen.Writeln('         þ Collect keys to unlock doors, which usually block the stairs.')
    screen.Writeln('         þ The faster monsters are the most dangerous to touch--they will knock')
    screen.Writeln('           off three of your valuable gems.  The slowest creatures only take a')
    screen.Writeln('           single gem from you, and the medium speed monsters take two.')
    screen.Writeln
    screen.Writeln('   Some levels have a Magical Gravity that will pull you downward!  On these')
    screen.Writeln(' levels the game is played as if viewing the level from a side angle.  On')
    screen.Writeln(' these levels you can only move upward by using a rope, a secret tunnel, or')
    screen.Writeln(' by using a teleport scroll.  These unique "Sideways Levels" may take a')
    screen.Writeln(' little getting used to, but are well worth the effort.  At the beginning of')
    screen.Writeln(' a "sideways" level a message at the bottom of the screen will alert you.')
    screen.Flash(27,25,'Press any key to continue.')
    
    #Screen3
    screen.ClearScreen()
    window.fill(COLORS[1])
    screen.Bak(1,0)
    screen.GotoXY(32,2)
    screen.Col(14,7)
    screen.Writeln('THE INSTRUCTIONS')

    screen.GotoXY(32,3)
    screen.Writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')

    screen.GotoXY(1,5)
    screen.Col(15,7)
    screen.Writeln("   Here are some brief descriptions of the most common objects that you are")
    screen.Writeln(' likely to find in the Kingdom of Kroz:')
    screen.Writeln("")
    
    screen.Write(  '      ')
    screen.Col(14,15)
    screen.Write("Player")
    screen.Col(15,7)
    screen.Writeln(' - this is you, a dauntless archaeologist without peer')
           
    screen.Write(  '      ')
    screen.Col(12,7)
    screen.Write("#142")
    screen.Col(15,7)
    screen.Writeln(' - red creatures move slow and only knock off 1 gem when touched')
           
    screen.Write(  '      ')
    screen.Col(10,7)
    screen.Write("#153")
    screen.Col(15,7)
    screen.Writeln(' - green creatures move faster and knock off 2 gems when touched')
           
    screen.Write(  '      ')
    screen.Col(9,7)
    screen.Write("#234")
    screen.Col(15,7)
    screen.Writeln(' - blue creatures move fastest and knock off 3 gems when touched')
           
    screen.Write(  '      ')
    screen.Col(15,7)
    screen.Write("Gem")
    screen.Col(15,7)
    screen.Writeln(' - collect all the gems you can to survive creature attacks')
           
    screen.Write(  '      ')
    screen.Write("Whip")
    screen.Writeln(' - whips are used to wipe out creatures and smash certain walls')
           
    screen.Write(  '      ')
    screen.Col(13,7)
    screen.Write("Teleport")
    screen.Col(15,7)
    screen.Writeln(' - teleport spells will magically transport you to a random place')
           
    screen.Write(  '      ')
    screen.Col(14,7)
    screen.Bak(4,0)
    screen.Write("Chest")
    screen.Bak(1,0)
    screen.Col(15,7)
    screen.Writeln(' - chests contain a random number of gems and whips')
           
    screen.Write(  '      ')
    screen.Col(12,15)
    screen.Write("Key")
    screen.Col(15,7)
    screen.Write(' - collect keys to go through doors (')
    screen.Col(3,0)
    screen.Bak(5,7)
           
    screen.Write("door")
    screen.Col(15,7)
    screen.Bak(1,0)
    screen.Writeln(')')
           
    screen.Write(  '      ')
    screen.Write("Power")
    screen.Writeln(' - collect these power rings to make your whips more powerful')
           
    screen.Write(  '      ')
    screen.Col(9,7)
    screen.Write("Tablet")
    screen.Col(15,7)
    screen.Writeln(' - these tablets will give you clues, advice and warnings')
           
    screen.Write(  '      ')
    screen.Write("Chance")
    screen.Writeln(' - this might be anything, including a big pouch of gems!')
           
    screen.Write(  '      ')
    screen.Col(1,1)
    screen.Bak(7,7)
    screen.Write("Stairs")
    screen.Col(15,7)
    screen.Bak(1,0)
    screen.Writeln(' - stairs take you to the next level deeper in Kroz')
           
    screen.Writeln("")
    screen.Writeln('   There are dozens and dozens of other objects to discover.  The best way')
    screen.Writeln(' to learn the usefulness of any new object is to touch it and read the brief')
    screen.Writeln(' message that appears at the bottom of the screen.')
    screen.Flash(27,25,'Press any key to continue.')


    #Screen 4
    screen.ClearScreen()
    window.fill(COLORS[1])
    screen.Bak(1,0)
    screen.GotoXY(32,2)
    screen.Col(14,7)
    screen.Writeln('MISCELLANEOUS')

    screen.GotoXY(32,3)
    screen.Writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
    
    screen.Writeln("")
    
    screen.Col(15,7)
    screen.Writeln("")
    screen.Writeln('  þ You can now save three different levels during a single game.  When you')
    screen.Writeln('    select the "save" command you will also be asked to enter a letter, either')
    screen.Writeln('    A, B or C.  If you just hit the space bar then A is the default selection.')
    screen.Writeln('    These letters do not refer to disk drives!  They actually refer to the file')
    screen.Writeln('    names used by the game.  The restore command lets use pick from A, B or C.')
    screen.Writeln("")
    screen.Writeln('  þ Sideways levels can be recognized by the pause message that appears at')
    screen.Writeln('    the bottom of the screen, which states that it''s a "sideways" level.')
    screen.Writeln("")
    screen.Writeln('  þ If you are tired of seeing the descriptions at the bottom of the screen')
    screen.Writeln('    that appear whenever you touch a new object, you can disable most of the')
    screen.Writeln('    messages by pressing the minus (-) key.  The plus key (+) resets messages.')
    screen.Writeln("")
    screen.Writeln('  þ Kingdom of Kroz II is a completely updated and improved version over the')
    screen.Writeln('    original version of Kingdom of Kroz.  If you desire to play the original')
    screen.Writeln('    Kingdom of Kroz, please send $7.50.  Over 17 levels are different!')
    screen.Flash(27,25,'Press any key to continue.')

    mainMenu()
    
def marketingScreen():
    screen.ClearScreen()
    window.fill(COLORS[1])
    screen.Bak(1,0)
    screen.GotoXY(29,2)
    screen.Col(14,7)
    screen.Writeln('THE MARKETING OF KROZ')
    screen.GotoXY(29,3)
    screen.Writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
    
    screen.Writeln("")
    screen.Col(15,7)
    
    screen.Writeln('   Kingdom of Kroz II is a user-supported game.  This means that the creator of')
    screen.Writeln(' this program relies on the appreciation of honest players to pay the game''s')
    screen.Writeln(' registration fee--$7.50.')
    screen.Writeln('   Payment of this fee entitles you to all the free help and hints you might')
    screen.Writeln(' need to enjoy the game.  All letters from registered users are answered')
    screen.Writeln(' within two days.  (Try to get this kind of support from commercial games!)')
    screen.Writeln('   Also, players can order the other Kroz sequels ONLY if this registration')
    screen.Writeln(' fee is paid.  ($7.50 each or $20 for The Lost Adventures of Kroz.)')
    screen.Writeln('   Everyone who orders (or registers) any of the other six Kroz games will also')
    screen.Writeln(' get a "Hints, Tricks and Scoring Secrets" guide, and "The Domain of Kroz" map.')
    screen.Writeln('   A single Kroz game takes several months to create, up to 200 hours per game!')
    screen.Writeln(' I can''t afford to devote this much time without receiving something in return.')
    screen.Writeln(' That is why I ask for this small fee, which is only necessary if you enjoy')
    screen.Writeln(' this game.  In other words, try before you buy.')
    screen.Writeln('   Even if you buy this game from a public domain or shareware library, I don''t')
    screen.Writeln(' receive any of that money.  You''re simply paying for "storage, distribution,')
    screen.Writeln(' disk, and handling."')
    screen.Writeln('   Note:  The current Apogee Software address will ALWAYS BE VALID.  Foreign')
    screen.Writeln(' orders are always welcome, please send U.S. funds/money orders only.')
    screen.Flash(27,25,'Press any key to continue.')

    mainMenu()

def storyScreen():  
    
    #Screen 1
    screen.ClearScreen()
    window.fill(COLORS[1])
    screen.Bak(1,0)
    screen.GotoXY(29,2)
    screen.Col(14,7)
    screen.Writeln('THE STORY BEHIND KROZ')
    screen.GotoXY(29,3)
    screen.Writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
    
    screen.Writeln("")
    screen.Col(15,7)
    screen.Writeln('   The original Kroz Trilogy (consisting of Caverns of Kroz, Dungeons of Kroz,')
    screen.Writeln(' and Kingdom of Kroz) was developed after I spent many hours playing another')
    screen.Writeln(' explore-the-levels type game titled Rogue.  I never could finish Rogue,')
    screen.Writeln(' though, because the game relied too much on luck and random occurrences.')
    screen.Writeln('   The name "Kroz" is actually Zork (an Infocom text adventure) spelled in')
    screen.Writeln(' reverse.  Many players still inquire about this bit of trivia.  The game was')
    screen.Writeln(' first designed without predefined level layouts, meaning every level was a')
    screen.Writeln(' random placement of creatures and play field objects.  New objects, like')
    screen.Writeln(' spells, lava, doors, etc., were added quickly as the first Kroz game took')
    screen.Writeln(' shape, including the ability to have predefined level floor plans.')
    screen.Writeln('   My main objective was to create a game that wasn''t all fast paced action,')
    screen.Writeln(' but also included strategy and puzzle solving.  Kingdom of Kroz was entered')
    screen.Writeln(' in a national programming contest in 1988 and took top honors in the game')
    screen.Writeln(' category, and number two overall (beaten by a spreadsheet program.)')
    screen.Writeln('   The latest Kroz games have been greatly re-designed and re-programmed, but')
    screen.Writeln(' the familiar appearance has been mostly maintained.  You will discover new')
    screen.Writeln(' dangers, creatures and objects in your adventures below.')
    screen.Writeln('   Thanks to all the players of Kroz who contributed dozens of suggestions,')
    screen.Writeln(' ideas and improvements that were incorporated in later versions of Kroz.')
    screen.Flash(27,25,'Press any key to continue.');

    #Screen 2
    screen.ClearScreen()
    window.fill(COLORS[1])
    screen.Bak(1,0)
    screen.GotoXY(29,2)
    screen.Col(14,7)
    screen.Writeln('THE STORY BEHIND KROZ')
    screen.GotoXY(29,3)
    screen.Writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
    
    screen.Writeln("")
    screen.Col(15,7)
    screen.Writeln('   Kroz is a hobby that''s gotten out of control!')
    screen.Writeln('   Kroz is truly a phenomenon in the user-supported software market.  The')
    screen.Writeln(' overwhelming success of the original Kroz games was completely unexpected.')
    screen.Writeln(' Most (probably 99%) of all "shareware" games are not profitable for their')
    screen.Writeln(' creator.  This is a well-known fact among the community of shareware game')
    screen.Writeln(' authors, and one that I''ve verified by speaking to many other games de-')
    screen.Writeln(' signers.  Most people simply don''t register games.')
    screen.Writeln('   Through my research the Kroz games are the only user-supported games that')
    screen.Writeln(' generate a substantial amount of registrations and orders for it''s creator,')
    screen.Writeln(' namely, Scott Miller (me).  I don''t know what cord I''ve struck with players,')
    screen.Writeln(' but everyday I receive fascinating and appreciative letters from players')
    screen.Writeln(' telling me how much they enjoy the Kroz games.')
    screen.Writeln('   Thanks to Kroz I now know what a mutual fund is, but on the downside my')
    screen.Writeln(' taxes require a book two inches thick to figure out.')
    screen.Writeln('   Will Kroz ever end?  I thought that THE FINAL CRUSADE would be the closing')
    screen.Writeln(' chapter--but a flood of letters demanding more proved that I''m a pushover.')
    screen.Writeln(' I guess as long as the letters keep coming, I''ll continue to make Kroz games.')
    screen.Writeln(' After all, Kroz is like my second home now, one that I like to visit often...')
    screen.Writeln('                                                        -- Scott Miller')
    screen.Flash(27,25,'Press any key to continue.')
    
    mainMenu()
    
def originalScreen():
    screen.ClearScreen()
    window.fill(COLORS[1])
    screen.Bak(1,0)
    screen.GotoXY(29,2)
    screen.Col(14,7)
    screen.Writeln('THE ORIGINAL KROZ GAMES')
    screen.GotoXY(29,3)
    screen.Writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
    
    screen.Writeln("")
    screen.Col(15,7)
    
    screen.Writeln('   The Lost Adventures of Kroz is the latest addition to the Kroz family of')
    screen.Writeln(' games.  Before this game there are six more Kroz volumes, separated into two')
    screen.Writeln(' triligies:  The Kroz Trilogy and The Super Kroz Trilogy.')
    screen.Writeln('   The original Kroz Trilogy was such a surprising success that I decided to')
    screen.Writeln(' created a second "Super Kroz" trilogy.  The first three original Kroz')
    screen.Writeln(' games are:   þ Kingdom of Kroz  þ Caverns of Kroz  þ Dungeons of Kroz.')
    screen.Writeln(' All three are still available and are constantly being updated and improved.')
    screen.Writeln('   The original Kroz Trilogy games can be purchased for $7.50 each, or all 3')
    screen.Writeln(' for $20 (these prices include postage, disks, and handling).')
    screen.Writeln('   Only Kingdom of Kroz can be placed in a shareware library for distribution,')
    screen.Writeln(' and the other two can only be ordered from Apogee Software Productions.')
    screen.Writeln('   The Super Kroz Trilogy volumes are revamped and greatly improved.  They are')
    screen.Writeln(' þ Return to Kroz  þ Temple of Kroz  þ The Final Crusade of Kroz.  The last')
    screen.Writeln(' three volumes were supposed to be the end of Kroz, but the mail kept coming')
    screen.Writeln(' and again I was impelled to create another Kroz adventure.')
    screen.Writeln('   All Kroz games work on all monitors, either graphics or monochrome systems.')
    screen.Writeln(' Plus, they only rely on keyboard control, and have slow-down routines that')
    screen.Writeln(' permit them to function correctly on any speed IBM PC compatible computer.')
    screen.Flash(27,25,'Press any key to continue.')
    
    mainMenu()
    
def aboutScreen():
    screen.ClearScreen()
    window.fill(COLORS[1])
    screen.Bak(1,0)
    screen.GotoXY(29,2)
    screen.Col(14,7)
    screen.Writeln('ABOUT THE AUTHOR')
    screen.GotoXY(29,3)
    screen.Writeln('ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ')
    
    screen.Writeln("")
    screen.Col(15,7)
    
    screen.Writeln('   Scott Miller, the creator of all the Kroz games, along with Supernova, Trek')
    screen.Writeln(' Trivia and Beyond the Titanic (all shareware games) began programming in high')
    screen.Writeln(' school in 1975.  Since then he''s created over 100 games and has had dozens')
    screen.Writeln(' publishered by BIG BLUE DISK, I.B.Magazette and Keypunch Software.')
    screen.Writeln("")
    screen.Writeln('   For over three years he wrote two weekly computer columns for the Dallas')
    screen.Writeln(' Morning News, one of the nation''s largest newspapers.  He also co-authored')
    screen.Writeln(' a video game strategy book titled, "Shootout: Beating the Video Games."')
    screen.Writeln(' Scott has written articles for COMPUTE!''s PC and PCjr Magazine and is a')
    screen.Writeln(' software reviewer with COMPUTE! Publications.')         
    screen.Writeln('')
    screen.Writeln('   Hobbies include softball, running, tennis, karate (1st degree black belt),')
    screen.Writeln(' drumming, rock music, science fiction, and creating new computer games.')
    screen.Writeln(' Favorite computer games are M.U.L.E., Jumpman, Planetfall, Enchanter, Zork,')
    screen.Writeln(' Spelunker, and Archon.  All are games of strategy, with action secondary.')
    screen.Writeln("")
    screen.Writeln('   Scott creates all Apogee Software programs on an AST Premium 80386 (20 Mhz)')
    screen.Writeln(' equipped with VGA graphics, a NEC MultiSync II and an HP LaserJet series II.')
    screen.Writeln(' The cost to market each Kroz game to the many shareware libraries and BBS''s')
    screen.Writeln(' is over $2000 per game.  All of the appreciative letters make it worth it!')
    screen.Flash(27,25,'Press any key to continue.')

    mainMenu()

# Test programs
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