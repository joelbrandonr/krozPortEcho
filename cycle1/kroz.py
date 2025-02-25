"""Caleb Mathurin
   February 3, 2025 - February 10, 2025
   Kingdom of Kroz 2 Recreation - For CS 370: Cycle 1"""
import pygame

pygame.init()
pygame.font.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
PLAY_WIDTH = 512
PLAY_HEIGHT = 370

pygame.display.set_caption("KINGDOM OF FRAUZ 2")

#p_x = 8
#p_y = 15

p_x = (PLAY_WIDTH // 2)
p_y = (WINDOW_HEIGHT // 2) - 24

p_width = 8
p_height = 16

TILE_MAP = {'X': 'block',
            'W': 'whip',
            'L': 'stairs',
            'C': 'chest',
            '+': 'gem',
            'T': 'teleport',
            '#': 'wall',
            '1': 'enemy1',
            '2': 'enemy2'}

level_1 = ['W W W W             2 2 2 2 2  C  2 2 2 2 2              W W W W',
           'XXXXXXXXXXXXXXXXXXX###########   ###########XXXXXXXXXXXXXXXXXXXX',
           ' 1           1                               1                  ',
           '                                    1            XX         1   ',
           '       1            1                           XXXX            ',
           '#        XX                    +                 XX            #',
           '##      XXXX  1                +          1          1        ##',
           'T##      XX               2    +    2                        ##T',
           'T1##                       W   +   W                        ##1T',
           'T########X                 WX     XW             1    X########T',
           '.        X                2WX  P  XW2                 X        .',
           'T########X         1       WX     XW                  X########T',
           'T1##                       W   +   W         1              ##1T',
           'T##                       2    +    2                        ##T',
           '##   1                         +                      XX      ##',
           '#       XX      1              +                 1   XXXX     1#',
           '       XXXX                 ##   ##                   XX        ',
           '1       XX                 ##     ##     1        1           1 ',
           '                    1#######       ########                     ',
           '    1         ########11111  +++++  111111########              ',
           'WW     ########+++++        #######         WWWWW########1    WW',
           '########                     2 2 2                     C########',
           'L2  +  X      #kingdom#of#kroz#ii#by#scott#miller#      X  +  2L']

font = pygame.font.Font("RobotoMono-Regular.ttf", 15)
text_surface = font.render('iiiiiiiiiiiiiiii', False, (170, 85, 0))


cursor = (0,0)
def GotoXY(x, y):
    if x not in range(0, 80) or y not in range(0, 25):
        raise ValueError("GotoXY out of bounds.")
    cursor_x = x * 8
    cursor_y = y * 16
    cursor = (x, y)

font = pygame.font.Font("RobotoMono-Regular.ttf", 15)
def Write(text, r, g, b):
    txt = font.render(text, False, (r, g, b))
    window.blit(txt, cursor)

level_draw_x = 8
level_draw_y = 16
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and p_x > 8:
        p_x -= p_width
    if keys[pygame.K_RIGHT] and p_x < 520 - p_width:
        p_x += p_width
    if keys[pygame.K_UP] and p_y > 16:
        p_y -= p_height
    if keys[pygame.K_DOWN] and p_y < 384 - p_height:
        p_y += p_height

    window.fill((0, 0, 0))

    pygame.draw.rect(window, (0, 0, 255), (528, 0, 112, 400)) #HUD

    pygame.draw.rect(window, (0, 255, 0), (520, 0, 8, 400)) #right border
    pygame.draw.rect(window, (0, 255, 0), (0, 0, 8, 400)) #left border
    pygame.draw.rect(window, (0, 255, 0), (8, 0, 512, 16)) #top border
    pygame.draw.rect(window, (0, 255, 0), (8, 384, 512, 16)) #bottom border

    for line in level_1:
        for element in line:
            if element == 'X':
                pygame.draw.rect(window, (255, 85, 0), (level_draw_x, level_draw_y, 8, 16))
            if element == 'W':
                pygame.draw.rect(window, (255, 255, 255), (level_draw_x, level_draw_y, 8, 16))
            if element == 'L':
                pygame.draw.rect(window, (170, 170, 170), (level_draw_x, level_draw_y, 8, 16))
            if element == 'C':
                pygame.draw.rect(window, (170, 0, 0), (level_draw_x, level_draw_y, 8, 16))
            if element == '+':
                pygame.draw.rect(window, (0, 170, 0), (level_draw_x, level_draw_y, 8, 16))
            if element == 'T':
                pygame.draw.rect(window, (255, 85, 255), (level_draw_x, level_draw_y, 8, 16))
            if element == '#':
                pygame.draw.rect(window, (170, 85, 0), (level_draw_x, level_draw_y, 8, 16))
            if element == '1':
                pygame.draw.rect(window, (255, 85, 85), (level_draw_x, level_draw_y, 8, 16))
            if element == '2':
                pygame.draw.rect(window, (85, 255, 85), (level_draw_x, level_draw_y, 8, 16))
            level_draw_x += 8
        level_draw_x = 8
        level_draw_y += 16
    level_draw_y = 16

    pygame.draw.rect(window, (255, 235, 59), (p_x, p_y, p_width, p_height))  # draw player

    GotoXY(4,24)
    Write("bingo was his nameo", 255, 0, 0)

    pygame.display.update()

pygame.quit()


