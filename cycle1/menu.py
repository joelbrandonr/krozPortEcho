"""Joel-Brandon Rivera
Cycle 1 Menu's and Title Screen"""

import pygame
import os
import time
import sys
import random

# Window size
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 400

def draw_kroz_logo(window, font, window_width, y_pos, color):
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
        text = font.render(line, True, color)
        window.blit(text, (20, y_pos + i * 25))  # Adjust spacing as needed

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

def home_screen(window, font):
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
                    window.fill((0, 0, 0))
                    title_text = font.render("KINGDOM OF KROZ 2", True, (66, 66, 200))
                    window.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 20))
                    question_text = font.render("Color or Monochrome (C/M)?", True, (255, 255, 255))
                    qpos = (WINDOW_WIDTH // 2 - question_text.get_width() // 2, 150)
                    window.blit(question_text, qpos)
                    input_surface = font.render(user_input, True, (255, 255, 255))
                    window.blit(input_surface, (qpos[0] + question_text.get_width() + 10, qpos[1]))
                    pygame.display.update()
                    pygame.time.delay(500)
                    running = False

        window.fill((0, 0, 0))
        title_text = font.render("KINGDOM OF KROZ 2", True, (66, 66, 200))
        window.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 20))
        question_text = font.render("Color or Monochrome (C/M)?", True, (255, 255, 255))
        qpos = (WINDOW_WIDTH // 2 - question_text.get_width() // 2, 150)
        window.blit(question_text, qpos)
        display_text = (user_input if user_input else "C") + ("_" if show_cursor else "")
        input_surface = font.render(display_text, True, (255, 255, 255))
        window.blit(input_surface, (qpos[0] + question_text.get_width() + 10, qpos[1]))
        pygame.display.update()

    return True if user_input.upper() == "C" else False

def computer_speed_screen(window, font, is_color):
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
                    window.fill((0, 0, 0))
                    title_text = font.render("KINGDOM OF KROZ 2", True, (66, 66, 200))
                    window.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 20))
                    question_text = font.render("Slow or Fast PC (S/F)?", True, (255, 255, 255))
                    qpos = (WINDOW_WIDTH // 2 - question_text.get_width() // 2, 150)
                    window.blit(question_text, qpos)
                    explanation = ("If you have an older PC choose 'S' for Slow. "
                                   "If you have a faster PC choose 'F'. (Default = Slow)")
                    wrapped = wrap_text(explanation, font, WINDOW_WIDTH - 100)
                    for i, line in enumerate(wrapped):
                        line_surface = font.render(line, True, (128, 128, 128))
                        window.blit(line_surface, (WINDOW_WIDTH // 2 - line_surface.get_width() // 2, 210 + i * 35))
                    input_surface = font.render(user_input, True, (255, 255, 255))
                    window.blit(input_surface, (qpos[0] + question_text.get_width() + 10, qpos[1]))
                    pygame.display.update()
                    pygame.time.delay(500)
                    running = False

        window.fill((0, 0, 0))
        title_text = font.render("KINGDOM OF KROZ 2", True, (66, 66, 200))
        window.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 20))
        question_text = font.render("Slow or Fast PC (S/F)?", True, (255, 255, 255))
        qpos = (WINDOW_WIDTH // 2 - question_text.get_width() // 2, 150)
        window.blit(question_text, qpos)
        explanation = ("If you have an older PC choose 'S' for Slow. "
                       "If you have a faster PC choose 'F'. (Default = Slow)")
        wrapped = wrap_text(explanation, font, WINDOW_WIDTH - 100)
        for i, line in enumerate(wrapped):
            line_surface = font.render(line, True, (128, 128, 128))
            window.blit(line_surface, (WINDOW_WIDTH // 2 - line_surface.get_width() // 2, 210 + i * 35))
        display_text = (user_input if user_input else "S") + ("_" if show_cursor else "")
        input_surface = font.render(display_text, True, (255, 255, 255))
        window.blit(input_surface, (qpos[0] + question_text.get_width() + 10, qpos[1]))
        pygame.display.update()

    return 1 if user_input.upper() == "F" else 3

def kingdom3_title(window, font):
    # Simple Kingdom3 title and menu screen
    window.fill((0, 0, 0))
    pres_text = font.render("Apogee Software Presents", True, (255, 255, 255))
    window.blit(pres_text, (WINDOW_WIDTH // 2 - pres_text.get_width() // 2, 20))
    pygame.display.update()
    pygame.time.delay(1500)

    #flahes logo
    for _ in range(10):
        window.fill((0, 0, 0))
        rand_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        
        # Draw the flashing KROZ logo
        draw_kroz_logo(window, font, WINDOW_WIDTH, 80, rand_color)
        
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
        window.fill((0, 0, 0))
        title_text = font.render("KINGDOM OF KROZ II", True, (66, 66, 200))
        window.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 20))
        start_y = 100
        for opt in menu_options:
            option_str = f"{opt[0]}) {opt[1]}"
            rendered_opt = font.render(option_str, True, (255, 255, 255))
            window.blit(rendered_opt, (WINDOW_WIDTH // 2 - rendered_opt.get_width() // 2, start_y))
            start_y += 40
        
        prompt_text = font.render("Your choice (B/I/M/S/O/A)?", True, (255, 255, 255))
        window.blit(prompt_text, (WINDOW_WIDTH // 2 - prompt_text.get_width() // 2, start_y + 20))
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
            window.fill((0, 0, 0))
            descent_text = font.render("Beginning descent...", True, (255, 255, 255))
            window.blit(descent_text, (WINDOW_WIDTH // 2 - descent_text.get_width() // 2, WINDOW_HEIGHT // 2))
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
            window.fill((0, 0, 0))
            y = 50
            for line in lines:
                rendered_line = font.render(line, True, (255, 255, 255))
                window.blit(rendered_line, (WINDOW_WIDTH // 2 - rendered_line.get_width() // 2, y))
                y += 30
            pygame.display.update()
            waiting_detail = True
            while waiting_detail:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        waiting_detail = False
                        break
                pygame.time.delay(100)

def final_screen(window, font, is_color, speed_value):
    # Show the chosen settings for a short time
    window.fill((0, 0, 0))
    final_text = f"Settings: {'Color' if is_color else 'Monochrome'}, {'Fast' if speed_value == 1 else 'Slow'} PC"
    text_surface = font.render(final_text, True, (255, 255, 255))
    window.blit(text_surface, (WINDOW_WIDTH // 2 - text_surface.get_width() // 2, WINDOW_HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("KINGDOM OF KROZ 2")
    FONT_PATH = os.path.join(os.path.dirname(__file__), 'fonts')
    TITLE_FONT = os.path.join(FONT_PATH, 'RobotoMono-Regular.ttf')
    font = pygame.font.Font(TITLE_FONT, 20)

    is_color = home_screen(window, font)
    speed_value = computer_speed_screen(window, font, is_color)
    kingdom3_title(window, font)
    final_screen(window, font, is_color, speed_value)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
