import pygame
from pygame.locals import *
import os

# Constants from original Kroz
PLAYER_CHAR = '☺'  # Classic roguelike player character
WALL_CHAR = '█'  # Unicode full block character
EMPTY_CHAR = ' '

# Original Kroz used specific tile IDs
NULL = 0
SLOW = 1
MEDIUM = 2
FAST = 3
WALL = 4
PLAYER_ID = 40

class KrozGame:
    def __init__(self):
        pygame.init()
        # Set console-like dimensions (close to original)
        os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
        self.char_width = 16  # Approximate size for font
        self.char_height = 16
        self.grid_width = 40  # Original game dimensions
        self.grid_height = 25
        self.screen = pygame.display.set_mode((
            self.grid_width * self.char_width,
            self.grid_height * self.char_height
        ))
        pygame.display.set_caption("Kingdom of Kroz II")
        
        # Initialize game font (try to match original DOS font)
        self.font = pygame.font.SysFont('Courier New', 16, bold=True)
        
        # Create playfield array (using original null values)
        self.playfield = [[NULL for x in range(self.grid_width)] 
                         for y in range(self.grid_height)]
        
        # Player position (PX, PY in original)
        self.px = 20
        self.py = 12
        self.replacement = NULL  # Original replacement variable
        
        # Timing variables from original
        self.skip_time = 0
        self.fast_pc = False  # Original FastPC variable
        
    def create_level(self):
        """Creates a level with obstacles similar to original Kroz"""
        # Clear the playfield
        self.playfield = [[NULL for x in range(self.grid_width)] 
                         for y in range(self.grid_height)]
        
        # Add border walls (like original)
        for x in range(self.grid_width):
            self.playfield[0][x] = WALL
            self.playfield[self.grid_height-1][x] = WALL
        for y in range(self.grid_height):
            self.playfield[y][0] = WALL
            self.playfield[y][self.grid_width-1] = WALL
        
        # Add some maze-like obstacles
        # Vertical walls
        for y in range(5, 15):
            self.playfield[y][10] = WALL
            self.playfield[y][30] = WALL
            
        # Horizontal walls
        for x in range(10, 20):
            self.playfield[8][x] = WALL
            self.playfield[18][x] = WALL
            
        # Small room
        for y in range(12, 15):
            for x in range(15, 25):
                if y in (12, 14) or x in (15, 24):
                    self.playfield[y][x] = WALL
                    
        # Add some single wall blocks for variety
        wall_positions = [(5, 5), (5, 35), (20, 5), (20, 35),
                         (15, 20), (7, 25), (18, 28)]
        for y, x in wall_positions:
            self.playfield[y][x] = WALL
            
        # Place player
        self.playfield[self.py][self.px] = PLAYER_ID

    def move(self, dx, dy):
        """Direct port of original move procedure"""
        new_x = self.px + dx
        new_y = self.py + dy
        
        # Check bounds (matching original)
        if (new_x < 1 or new_x >= self.grid_width-1 or 
            new_y < 1 or new_y >= self.grid_height-1):
            return
            
        new_pos_value = self.playfield[new_y][new_x]
        
        # Original walkable tiles
        if new_pos_value in [NULL, 32, 33, 37, 39, 41, 44, 47]:
            # Handle replacement like original
            if self.replacement is not None:
                self.playfield[self.py][self.px] = self.replacement
            else:
                self.playfield[self.py][self.px] = NULL
                
            self.px = new_x
            self.py = new_y
            self.replacement = self.playfield[new_y][new_x]
            self.playfield[new_y][new_x] = PLAYER_ID

    def process_input(self):
        """Matches original Pascal input processing"""
        keys = pygame.key.get_pressed()
        
        # Original keycodes mapped to Pygame
        if keys[K_KP8] or keys[K_UP]:      # 172 - North
            self.move(0, -1)
        if keys[K_KP2] or keys[K_DOWN]:    # 180 - South
            self.move(0, 1)
        if keys[K_KP6] or keys[K_RIGHT]:   # 177 - East
            self.move(1, 0)
        if keys[K_KP4] or keys[K_LEFT]:    # 175 - West
            self.move(-1, 0)
        if keys[K_KP7] or keys[K_q]:       # 171 - Northwest
            self.move(-1, -1)
        if keys[K_KP9] or keys[K_e]:       # 173 - Northeast
            self.move(1, -1)
        if keys[K_KP1] or keys[K_z]:       # 179 - Southwest
            self.move(-1, 1)
        if keys[K_KP3] or keys[K_c]:       # 181 - Southeast
            self.move(1, 1)

    def draw(self):
        """Draw the game state using character-based rendering"""
        self.screen.fill((0, 0, 0))  # Clear to black like original
        
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                char = EMPTY_CHAR
                color = (128, 128, 128)  # Default gray
                
                if self.playfield[y][x] == WALL:
                    char = WALL_CHAR
                elif self.playfield[y][x] == PLAYER_ID:
                    char = PLAYER_CHAR
                    color = (255, 255, 255)  # Player was bright in original
                
                if char != EMPTY_CHAR:
                    text = self.font.render(char, True, color)
                    self.screen.blit(text, 
                        (x * self.char_width, y * self.char_height))
        
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        move_timer = 0
        
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            
            # Control movement speed
            current_time = pygame.time.get_ticks()
            if current_time - move_timer >= 200:  # Adjust this number to control speed (higher = slower)
                self.process_input()
                move_timer = current_time
            
            self.draw()
            clock.tick(30)

if __name__ == '__main__':
    game = KrozGame()
    game.run()