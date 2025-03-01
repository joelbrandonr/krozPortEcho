"""Joel-Brandon Rivera
Cycle 1 Menu's and Title Screen"""

import pygame
import os
import time
import sys
import random
from screenFunctions import Screen, RED, WHITE  # Import the Screen class and color constants

# Window size
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 400

def draw_kroz_logo(screen, y_pos, color):
    """Draw the ASCII KROZ logo with random colors"""
    logo_lines = [
        "     ���     ���     ����������         �����������        �������������  (R)",
        "     ��۱�  ��۱��   ��۱������۱      ��۱��������۱        ���������۱��",
        "     ��۱� ��۱��    ��۱�   ��۱�     ��۱�     ��۱�            ��۱���",
        "     ████████████     █████   █████    ██████      █████           ███████",
        "     ██████████      ███████████████    █████       █████         ███████",
        "     ████████       ████████████     █████       █████        ███████",
        "     ████████        ████ ████        █████      ██████       ███████",
        "     ████████       █████  ████       █████     █████      ████████",
        "     ████ ████      █████   ████       █████████████     ████████████",
        "     ████  ████       ███     ███        █████████        ████████████",
        "     ████   ████",
        "     ████    █████████████████████████████████████████████████████████",
        "       ███      █████████████████████████████████████████████████████████"
    ]
    
    # Draw each line of the logo
    for i, line in enumerate(logo_lines):
        screen.write(line)
        screen.goto_xy(20, y_pos + i * 25 // 16)  # Adjust spacing as needed

def wrap_text(text, font, max_width):
    # Split text into lines that fit in max_width
    words = text.split(' ')
    lines = []
    cur_line = []
    cur_width = 0
    for word in words:
        word_surface = font.render(word + ' ', True, (255, 255, 255))
        word_width = word_surface.get_width()
        if cur_width + word_width <= max_width:
            cur_line.append(word)
            cur_width += word_width
        else:
            lines.append(' '.join(cur_line))
            cur_line = [word]
            cur_width = word_width
    if cur_line:
        lines.append(' '.join(cur_line))
    return lines

def home_screen(screen):
    # Ask if screen is Color or Monochrome (C/M)
    user_input = ""
    blink_timer = time.time()
    blink_interval = 0.5
    show_cursor = True
    running = True

    while running:
        pygame.time.delay(100)
        if time.time() - blink_timer > blink_interval:
            show_cursor = not show_cursor
            blink_timer = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_c, pygame.K_m]:
                    user_input = "C" if event.key == pygame.K_c else "M"
                    screen.window.fill((0, 0, 0))
                    screen.write("KINGDOM OF KROZ 2")
                    screen.goto_xy(WINDOW_WIDTH // 2 - 10, 20)
                    screen.write("Color or Monochrome (C/M)?")
                    screen.goto_xy(WINDOW_WIDTH // 2 - 10, 150)
                    screen.write(user_input)
                    pygame.display.update()
                    pygame.time.delay(500)
                    running = False

        screen.window.fill((0, 0, 0))
        screen.write("KINGDOM OF KROZ 2")
        screen.goto_xy(WINDOW_WIDTH // 2 - 10, 20)
        screen.write("Color or Monochrome (C/M)?")
        screen.goto_xy(WINDOW_WIDTH // 2 - 10, 150)
        display_text = (user_input if user_input else "C") + ("_" if show_cursor else "")
        screen.write(display_text)
        pygame.display.update()

    return True if user_input.upper() == "C" else False

def computer_speed_screen(screen, is_color):
    # Ask if PC is Fast or Slow (F/S)
    user_input = ""
    blink_timer = time.time()
    blink_interval = 0.5
    show_cursor = True
    running = True

    while running:
        pygame.time.delay(100)
        if time.time() - blink_timer > blink_interval:
            show_cursor = not show_cursor
            blink_timer = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_f, pygame.K_s]:
                    user_input = "F" if event.key == pygame.K_f else "S"
                    screen.window.fill((0, 0, 0))
                    screen.write("KINGDOM OF KROZ 2")
                    screen.goto_xy(WINDOW_WIDTH // 2 - 10, 20)
                    screen.write("Slow or Fast PC (S/F)?")
                    screen.goto_xy(WINDOW_WIDTH // 2 - 10, 150)
                    explanation = ("If you have an older PC choose 'S' for Slow. "
                                   "If you have a faster PC choose 'F'. (Default = Slow)")
                    wrapped = wrap_text(explanation, screen.font, WINDOW_WIDTH - 100)
                    for i, line in enumerate(wrapped):
                        screen.write(line)
                        screen.goto_xy(WINDOW_WIDTH // 2 - 10, 210 + i * 35 // 16)
                    screen.write(user_input)
                    pygame.display.update()
                    pygame.time.delay(500)
                    running = False

        screen.window.fill((0, 0, 0))
        screen.write("KINGDOM OF KROZ 2")
        screen.goto_xy(WINDOW_WIDTH // 2 - 10, 20)
        screen.write("Slow or Fast PC (S/F)?")
        screen.goto_xy(WINDOW_WIDTH // 2 - 10, 150)
        explanation = ("If you have an older PC choose 'S' for Slow. "
                       "If you have a faster PC choose 'F'. (Default = Slow)")
        wrapped = wrap_text(explanation, screen.font, WINDOW_WIDTH - 100)
        for i, line in enumerate(wrapped):
            screen.write(line)
            screen.goto_xy(WINDOW_WIDTH // 2 - 10, 210 + i * 35 // 16)
        display_text = (user_input if user_input else "S") + ("_" if show_cursor else "")
        screen.write(display_text)
        pygame.display.update()

    return 1 if user_input.upper() == "F" else 3

def kingdom3_title(screen):
    # Simple Kingdom3 title and menu screen
    screen.window.fill((0, 0, 0))
    screen.write("Apogee Software Presents")
    screen.goto_xy(WINDOW_WIDTH // 2 - 10, 20)
    pygame.display.update()
    pygame.time.delay(1500)

    # Flashes logo
    for _ in range(10):
        screen.window.fill((0, 0, 0))
        rand_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        
        # Draw the flashing KROZ logo
        draw_kroz_logo(screen, 80, rand_color)
        
        pygame.display.update()
        pygame.time.delay(200)

    # Menu options
    menu_options = [
        ("B", "Begin your descent into Kroz..."),
        ("I", "Instructions"),
        ("M", "Marketing Kroz"),
        ("S", "Story Behind Kroz"),
        ("O", "Original Kroz Games"),
        ("A", "About the Author")
    ]

    start_game = False
    while not start_game:
        screen.window.fill((0, 0, 0))
        screen.write("KINGDOM OF KROZ II")
        screen.goto_xy(WINDOW_WIDTH // 2 - 10, 20)
        start_y = 100
        for opt in menu_options:
            option_str = f"{opt[0]}) {opt[1]}"
            screen.write(option_str)
            screen.goto_xy(WINDOW_WIDTH // 2 - 10, start_y)
            start_y += 40
        
        screen.write("Your choice (B/I/M/S/O/A)?")
        screen.goto_xy(WINDOW_WIDTH // 2 - 10, start_y + 20)
        pygame.display.update()
        
        choice = None
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    ch = event.unicode.upper()
                    if ch in ["B", "I", "M", "S", "O", "A"]:
                        choice = ch
                        waiting = False
                        break
            pygame.time.delay(100)
        
        if choice == "B":
            screen.window.fill((0, 0, 0))
            screen.write("Beginning descent...")
            screen.goto_xy(WINDOW_WIDTH // 2 - 10, WINDOW_HEIGHT // 2)
            pygame.display.update()
            for i in range(10, 0, -1):
                pygame.time.delay(100)
            start_game = True
        else:
            details = {
                "I": "Instructions:\nKroz is an adventure game...\n(Press any key)",
                "M": "Marketing Kroz:\nUser-supported game...\n(Press any key)",
                "S": "Story Behind Kroz:\nAn epic tale...\n(Press any key)",
                "O": "Original Kroz Games:\nThe first trilogy...\n(Press any key)",
                "A": "About the Author:\nScott Miller, creator of Kroz...\n(Press any key)"
            }
            detail_text = details.get(choice, "")
            lines = detail_text.split("\n")
            screen.window.fill((0, 0, 0))
            y = 50
            for line in lines:
                screen.write(line)
                screen.goto_xy(WINDOW_WIDTH // 2 - 10, y)
                y += 30
            pygame.display.update()
            waiting_detail = True
            while waiting_detail:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        waiting_detail = False
                        break
                pygame.time.delay(100)

def final_screen(screen, is_color, speed_value):
    # Show the chosen settings for a short time
    screen.window.fill((0, 0, 0))
    final_text = f"Settings: {'Color' if is_color else 'Monochrome'}, {'Fast' if speed_value == 1 else 'Slow'} PC"
    screen.write(final_text)
    screen.goto_xy(WINDOW_WIDTH // 2 - 10, WINDOW_HEIGHT // 2)
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    pygame.init()
    screen = Screen(WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.display.set_caption("KINGDOM OF KROZ 2")

    is_color = home_screen(screen)
    speed_value = computer_speed_screen(screen, is_color)
    kingdom3_title(screen)
    final_screen(screen, is_color, speed_value)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()