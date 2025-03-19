import pygame
import sys
import os

# Import menu screens from menu_screens.py
from menu import (colorScreen, speedScreen, logoScreen, 
                        difficultyScreen, registrationScreen, mainMenu,
                        instructionScreen, marketingScreen, storyScreen,
                        originalScreen, aboutScreen)

# Import game functionality from gameState.py
from gameState import run_kroz_game

def main():
    """Main entry point that connects menu screens with gameplay"""
    pygame.init()
    pygame.font.init()
    
    # Initialize variables to store game settings
    game_settings = {
        "color_mode": None,
        "speed": None,
        "difficulty": None
    }
    
    # Run through menu screens sequence
    game_settings["color_mode"] = colorScreen()
    game_settings["speed"] = speedScreen()
    logoScreen()
    game_settings["difficulty"] = difficultyScreen()
    registrationScreen()
    
    # Main menu selection
    menu_choice = mainMenu()
    
    # Handle menu choice
    if menu_choice == 'begin':
        print("Starting game...")
        # Clear screen and shut down the menu system
        pygame.display.quit()
        
        # Initialize a new pygame window for the game
        pygame.init()
        
        # Start the game with the chosen settings
        # You may need to modify run_kroz_game to accept these parameters
        run_kroz_game()
    
    # Game has ended - clean up and exit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()