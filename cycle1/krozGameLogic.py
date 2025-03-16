import random
import time
import numpy as np
import pygame

#constants from original Kroz file
NULL = 0
SLOW = 1
MEDIUM = 2
FAST = 3
WALL = 4
PLAYER_ID = 40
MBLOCK_ID = 38

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()
        
    def sound(self, frequency):
        """Play sound indefinitely."""
        sample_rate = 44100
        duration = 1.0
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)
        audio_data = (audio_data * 32767).astype(np.int16)
        # Create stereo audio data by duplicating the mono data
        stereo_audio_data = np.column_stack((audio_data, audio_data))
        # Create a sound object
        sound = pygame.sndarray.make_sound(stereo_audio_data)
        sound.play(-1) # Play indefinitely
        
    def nosound(self):
        """Stop the sound."""
        pygame.mixer.stop()
        
    def delay(self, milliseconds):
        time.sleep(milliseconds/1000)
        
    def play(self, frequency1, frequency2, delay_length):
        if frequency1 <= frequency2:
            for x in range(frequency1, frequency2 + 1):
                self.sound(x)
                self.delay(delay_length)
        else:
            for x in range(frequency1, frequency2 - 1, -1): # down to frequency2
                self.sound(x)
                self.delay(delay_length)
        self.nosound()
        
    def FootStep(self, FastPC):
        for x in range (1, int(FastPC)*50+int(not FastPC)*23):
            self.sound(random.randint(0, 550)+350)
            self.delay(0.01) # added delay to compensate for fast CPU
        self.delay(2); # Added delay to compensate for fast CPU
        self.nosound()
        self.delay(120);
        for x in range(1, int(FastPC)*60+int(not FastPC)*30):
            self.sound(random.randint(0, 50)+150)
            self.nosound()
    
    def GrabSound(self, FastPC):
        for x in range(1, int(FastPC)*160+int(not FastPC)*65):
            self.sound(random.randint(0, 1000)+1000)
            self.delay(0.01) # added delay to compensate for fast CPU
        self.nosound()
        
    def BlockSound(self, FastPC):
        for x in range(60, 30, -1):
            self.sound(x)
            self.delay(1+int(FastPC)*2)
        self.nosound()
        
    def NoneSound(self):
        for x in range (1, 5):
            self.sound(400)
            self.delay(10)
            self.nosound()
            self.delay(10);
        self.sound(700)
        self.delay(10)
        self.nosound()
        self.delay(10);

class KrozGameLogic:
    def __init__(self, sound_player=None, playfield=None):
        #grid dimensions
        self.grid_width = 80  #original game dimensions
        self.grid_height = 25
        
        #creates playfield array or use the provided one
        if playfield:
            self.pf = playfield
        else:
            self.pf = [[NULL for x in range(self.grid_width)] 
                      for y in range(self.grid_height)]
        
        # Player position (PX, PY in original)
        self.px = 20
        self.py = 12
        self.replacement = NULL  # Original replacement variable
        
        # Game variables
        self.score = 0
        self.gems = 10
        self.sideways = False
        
        # Enemy tracking
        self.s_num = 0  # Number of slow enemies
        self.m_num = 0  # Number of medium enemies
        self.f_num = 0  # Number of fast enemies
        self.b_num = 0  # Number of moving blocks
        
        # Enemy position arrays (1-indexed as in original)
        self.sx = [None] * 100
        self.sy = [None] * 100
        self.mx = [None] * 100
        self.my = [None] * 100
        self.fx = [None] * 100
        self.fy = [None] * 100
        self.bx = [None] * 100
        self.by = [None] * 100
        
        # Timer array (controls when things happen)
        self.t = [0] * 10
        self.s_time = 8  # Speed settings for slow enemies
        self.m_time = 6  # Speed settings for medium enemies
        self.f_time = 4  # Speed settings for fast enemies
        self.b_time = 10  # Speed settings for blocks
        
        # Timing variables from original
        self.skip_time = 0
        self.fast_pc = True  # Original FastPC variable
        
        # Set sound player (use the one provided or create a new one)
        self.sound_player = sound_player if sound_player else SoundPlayer()
        
        # Game state flag
        self.game_over = False
        self.level_complete = False
    
    def set_playfield(self, playfield):
        """Set the playfield from an external source"""
        self.pf = playfield
        
    def set_player_position(self, x, y):
        """Set the player position"""
        # Make sure x and y are within valid range
        x = max(1, min(x, self.grid_width - 2))
        y = max(1, min(y, self.grid_height - 2))
        
        # Clear the player from their current position
        if self.pf[self.py][self.px] == PLAYER_ID:
            self.pf[self.py][self.px] = NULL
            
        # Set new position
        self.px = x
        self.py = y
        self.pf[y][x] = PLAYER_ID
        
    def add_enemy(self, enemy_type, x, y):
        """Add an enemy at a specific position"""
        # Make sure x and y are within valid range
        if not (0 <= x < self.grid_width and 0 <= y < self.grid_height):
            return
            
        if enemy_type == SLOW:
            self.s_num += 1
            self.sx[self.s_num] = x
            self.sy[self.s_num] = y
            self.pf[y][x] = SLOW
        elif enemy_type == MEDIUM:
            self.m_num += 1
            self.mx[self.m_num] = x
            self.my[self.m_num] = y
            self.pf[y][x] = MEDIUM
        elif enemy_type == FAST:
            self.f_num += 1
            self.fx[self.f_num] = x
            self.fy[self.f_num] = y
            self.pf[y][x] = FAST
        
    def move(self, dx, dy):
        """Direct port of original move procedure"""
        new_x = self.px + dx
        new_y = self.py + dy
        
        # Check bounds (matching original)
        if (new_x < 1 or new_x >= self.grid_width-1 or 
            new_y < 1 or new_y >= self.grid_height-1):
            return False
            
        new_pos_value = self.pf[new_y][new_x]
        
        # Original walkable tiles
        if new_pos_value in [NULL, 32, 33, 37, 39, 41, 44, 47]:
            # Handle replacement like original
            if self.replacement is not None:
                self.pf[self.py][self.px] = self.replacement
            else:
                self.pf[self.py][self.px] = NULL
                
            self.px = new_x
            self.py = new_y
            self.replacement = self.pf[new_y][new_x]
            self.pf[new_y][new_x] = PLAYER_ID
            return True
        
        # Wall or other obstacle
        return False

    def process_input(self, direction):
        """
        Process player movement based on direction
        direction should be one of: 'n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw'
        Returns True if movement was successful
        """
        if direction == 'n':
            return self.move(0, -1)
        elif direction == 's':
            return self.move(0, 1)
        elif direction == 'e':
            return self.move(1, 0)
        elif direction == 'w':
            return self.move(-1, 0)
        elif direction == 'nw':
            return self.move(-1, -1)
        elif direction == 'ne':
            return self.move(1, -1)
        elif direction == 'sw':
            return self.move(-1, 1)
        elif direction == 'se':
            return self.move(1, 1)
        else:
            return False
    
    def player_died(self, lost_gems=False):
        """Handle player death"""
        self.game_over = True
        return lost_gems
    
    def move_slow(self):
        """
        Handles movement of all slow enemies toward the player.
        """
        # Handle timing logic
        if self.t[6] > 0:
            if self.fast_pc:
                self.t[1] = 3
            else:
                self.t[1] = None  # Null in Pascal
        else:
            if self.t[4] < 1:
                self.t[1] = self.s_time
            else:
                self.t[1] = self.s_time * 5
        
        # Exit if no slow enemies
        if self.s_num < 1:
            return
        
        # Process each slow enemy
        for loop in range(1, self.s_num + 1):
            # Skip if this enemy is None
            if self.sx[loop] is None:
                continue
            
            # Check if enemy is still at expected position
            if self.pf[self.sy[loop]][self.sx[loop]] != SLOW:
                self.sx[loop] = None
                continue
            
            # Clear enemy from current position
            self.pf[self.sy[loop]][self.sx[loop]] = NULL
            
            # Calculate direction to move
            x_dir, y_dir = 0, 0
            
            # Horizontal movement
            if self.px < self.sx[loop]:
                self.sx[loop] -= 1
                x_dir = 1
            elif self.px > self.sx[loop]:
                self.sx[loop] += 1
                x_dir = -1
            
            # Vertical movement (unless in sideways mode)
            if not self.sideways:
                if self.py < self.sy[loop]:
                    self.sy[loop] -= 1
                    y_dir = 1
                elif self.py > self.sy[loop]:
                    self.sy[loop] += 1
                    y_dir = -1
            
            # Get position and handle what's at the new location
            x, y = self.sx[loop], self.sy[loop]
            
            # Bounds check
            if not (0 <= y < self.grid_height and 0 <= x < self.grid_width):
                self.sx[loop] = None
                continue
            
            # Handle different target tiles
            target_tile = self.pf[y][x]
            
            if target_tile == NULL or (68 <= target_tile <= 74):
                # Empty space or specific tiles
                self.sound_player.sound(20)
                self.sound_player.nosound()
                self.pf[y][x] = SLOW
                
            elif target_tile in [SLOW, MEDIUM, FAST, WALL]:
                # Walls and obstacles - move back and try again
                self.sx[loop] += x_dir
                self.sy[loop] += y_dir
                
                # Bounds check after moving back
                if (0 <= self.sy[loop] < self.grid_height and 
                    0 <= self.sx[loop] < self.grid_width):
                    self.pf[self.sy[loop]][self.sx[loop]] = SLOW
                else:
                    self.sx[loop] = None
                
            elif target_tile == PLAYER_ID:
                # Player collision
                self.sound_player.sound(400)
                self.sound_player.delay(25)
                self.sound_player.nosound()
                self.sx[loop] = None
                self.gems -= 1
                
                if self.gems < 0:
                    self.player_died(True)
                
            else:
                # Default case for any other tile
                self.sx[loop] += x_dir
                self.sy[loop] += y_dir
                
                # Bounds check after moving back
                if (0 <= self.sy[loop] < self.grid_height and 
                    0 <= self.sx[loop] < self.grid_width):
                    self.pf[self.sy[loop]][self.sx[loop]] = SLOW
                else:
                    self.sx[loop] = None
    
    def move_medium(self):
        """
        Handles movement of all medium-speed enemies toward the player.
        """
        # Handle timing logic
        if self.t[6] > 0:
            if self.fast_pc:
                self.t[2] = 3
            else:
                self.t[2] = None  # Null in Pascal
        else:
            if self.t[4] < 1:
                self.t[2] = self.m_time
            else:
                self.t[2] = self.m_time * 5
        
        # Exit if no medium enemies
        if self.m_num < 1:
            return
        
        # Process each medium enemy
        for loop in range(1, self.m_num + 1):
            # Skip if this enemy is None
            if self.mx[loop] is None:
                continue
            
            # Check if enemy is still at expected position
            if self.pf[self.my[loop]][self.mx[loop]] != MEDIUM:
                self.mx[loop] = None
                continue
            
            # Clear enemy from current position
            self.pf[self.my[loop]][self.mx[loop]] = NULL
            
            # Calculate direction to move
            x_dir, y_dir = 0, 0
            
            # Horizontal movement
            if self.px < self.mx[loop]:
                self.mx[loop] -= 1
                x_dir = 1
            elif self.px > self.mx[loop]:
                self.mx[loop] += 1
                x_dir = -1
            
            # Vertical movement (unless in sideways mode)
            if not self.sideways:
                if self.py < self.my[loop]:
                    self.my[loop] -= 1
                    y_dir = 1
                elif self.py > self.my[loop]:
                    self.my[loop] += 1
                    y_dir = -1
            
            # Get position and handle what's at the new location
            x, y = self.mx[loop], self.my[loop]
            
            # Bounds check
            if not (0 <= y < self.grid_height and 0 <= x < self.grid_width):
                self.mx[loop] = None
                continue
            
            # Handle different target tiles
            target_tile = self.pf[y][x]
            
            if target_tile == NULL or (68 <= target_tile <= 74):
                # Empty space or specific tiles
                self.sound_player.sound(20)
                self.sound_player.nosound()
                self.pf[y][x] = MEDIUM
                
            elif target_tile in [SLOW, MEDIUM, FAST, WALL]:
                # Walls and obstacles - move back and try again
                self.mx[loop] += x_dir
                self.my[loop] += y_dir
                
                # Bounds check after moving back
                if (0 <= self.my[loop] < self.grid_height and 
                    0 <= self.mx[loop] < self.grid_width):
                    self.pf[self.my[loop]][self.mx[loop]] = MEDIUM
                else:
                    self.mx[loop] = None
                
            elif target_tile == PLAYER_ID:
                # Player collision
                self.sound_player.sound(600)
                self.sound_player.delay(25)
                self.sound_player.nosound()
                self.mx[loop] = None
                self.gems -= 2  # Medium enemies take 2 gems
                
                if self.gems < 0:
                    self.player_died(True)
                
            else:
                # Default case for any other tile
                self.mx[loop] += x_dir
                self.my[loop] += y_dir
                
                # Bounds check after moving back
                if (0 <= self.my[loop] < self.grid_height and 
                    0 <= self.mx[loop] < self.grid_width):
                    self.pf[self.my[loop]][self.mx[loop]] = MEDIUM
                else:
                    self.mx[loop] = None
    
    def move_fast(self):
        """
        Handles movement of all fast enemies toward the player.
        """
        # Handle timing logic
        if self.t[6] > 0:
            if self.fast_pc:
                self.t[3] = 3
            else:
                self.t[3] = None  # Null in Pascal
        else:
            if self.t[4] < 1:
                self.t[3] = self.f_time
            else:
                self.t[3] = self.f_time * 5
        
        # Exit if no fast enemies
        if self.f_num < 1:
            return
        
        # Process each fast enemy
        for loop in range(1, self.f_num + 1):
            # Skip if this enemy is None
            if self.fx[loop] is None:
                continue
            
            # Check if enemy is still at expected position
            if self.pf[self.fy[loop]][self.fx[loop]] != FAST:
                self.fx[loop] = None
                continue
            
            # Clear enemy from current position
            self.pf[self.fy[loop]][self.fx[loop]] = NULL
            
            # Calculate direction to move
            x_dir, y_dir = 0, 0
            
            # Horizontal movement
            if self.px < self.fx[loop]:
                self.fx[loop] -= 1
                x_dir = 1
            elif self.px > self.fx[loop]:
                self.fx[loop] += 1
                x_dir = -1
            
            # Vertical movement (unless in sideways mode)
            if not self.sideways:
                if self.py < self.fy[loop]:
                    self.fy[loop] -= 1
                    y_dir = 1
                elif self.py > self.fy[loop]:
                    self.fy[loop] += 1
                    y_dir = -1
            
            # Get position and handle what's at the new location
            x, y = self.fx[loop], self.fy[loop]
            
            # Bounds check
            if not (0 <= y < self.grid_height and 0 <= x < self.grid_width):
                self.fx[loop] = None
                continue
            
            # Handle different target tiles
            target_tile = self.pf[y][x]
            
            if target_tile == NULL or (68 <= target_tile <= 74):
                # Empty space or specific tiles
                self.sound_player.sound(20)
                self.sound_player.nosound()
                self.pf[y][x] = FAST
                
            elif target_tile in [SLOW, MEDIUM, FAST, WALL]:
                # Walls and obstacles - move back and try again
                self.fx[loop] += x_dir
                self.fy[loop] += y_dir
                
                # Bounds check after moving back
                if (0 <= self.fy[loop] < self.grid_height and 
                    0 <= self.fx[loop] < self.grid_width):
                    self.pf[self.fy[loop]][self.fx[loop]] = FAST
                else:
                    self.fx[loop] = None
                
            elif target_tile == PLAYER_ID:
                # Player collision
                self.sound_player.sound(800)
                self.sound_player.delay(25)
                self.sound_player.nosound()
                self.fx[loop] = None
                self.gems -= 3  # Fast enemies take 3 gems
                
                if self.gems < 0:
                    self.player_died(True)
                
            else:
                # Default case for any other tile
                self.fx[loop] += x_dir
                self.fy[loop] += y_dir
                
                # Bounds check after moving back
                if (0 <= self.fy[loop] < self.grid_height and 
                    0 <= self.fx[loop] < self.grid_width):
                    self.pf[self.fy[loop]][self.fx[loop]] = FAST
                else:
                    self.fx[loop] = None
    
    def move_mblock(self):
        """
        Handles movement of all moving blocks toward the player.
        """
        # Set timer
        self.t[8] = self.b_time
        
        # Exit if no moving blocks
        if self.b_num < 1:
            return
        
        # Process each moving block
        for loop in range(1, self.b_num + 1):
            # Skip if this block is None
            if self.bx[loop] is None:
                continue
            
            # Check if block is still at expected position
            if self.pf[self.by[loop]][self.bx[loop]] != MBLOCK_ID:
                self.bx[loop] = None
                continue
            
            # Clear block from current position
            self.pf[self.by[loop]][self.bx[loop]] = NULL
            
            # Calculate direction to move
            x_dir, y_dir = 0, 0
            
            # Horizontal movement
            if self.px < self.bx[loop]:
                self.bx[loop] -= 1
                x_dir = 1
            elif self.px > self.bx[loop]:
                self.bx[loop] += 1
                x_dir = -1
            
            # Vertical movement (unless in sideways mode)
            if not self.sideways:
                if self.py < self.by[loop]:
                    self.by[loop] -= 1
                    y_dir = 1
                elif self.py > self.by[loop]:
                    self.by[loop] += 1
                    y_dir = -1
            
            # Get position
            x, y = self.bx[loop], self.by[loop]
            
            # Bounds check
            if not (0 <= y < self.grid_height and 0 <= x < self.grid_width):
                self.bx[loop] = None
                continue
            
            # Handle different target tiles
            target_tile = self.pf[y][x]
            
            if target_tile == NULL:
                # Empty space
                self.sound_player.sound(20)
                self.sound_player.delay(1)
                self.sound_player.nosound()
                self.pf[y][x] = MBLOCK_ID
            else:
                # Cannot move there, try to find another path
                self.bx[loop] += x_dir
                self.by[loop] += y_dir
                
                # Bounds check after moving back
                if (0 <= self.by[loop] < self.grid_height and 
                    0 <= self.bx[loop] < self.grid_width):
                    self.pf[self.by[loop]][self.bx[loop]] = MBLOCK_ID
                else:
                    self.bx[loop] = None

    def update(self):
        """Update game state for a single frame"""
        # Move enemies according to their speed
        self.move_slow()
        self.move_medium()
        self.move_fast()
        self.move_mblock()
        
        # Return game state
        return {
            'game_over': self.game_over,
            'level_complete': self.level_complete,
            'score': self.score,
            'gems': self.gems
        }
    
    def get_game_state(self):
        """Return the current game state for rendering"""
        return {
            'playfield': self.pf,
            'player_x': self.px,
            'player_y': self.py,
            'score': self.score,
            'gems': self.gems,
            'game_over': self.game_over,
            'level_complete': self.level_complete
        }

def run_kroz_game():
    """Run the full Kroz game with pygame visualization"""
    pygame.init()
    pygame.font.init()
    
    # Set up the window and display
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 400
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    PLAY_WIDTH = 512
    PLAY_HEIGHT = 370

    pygame.display.set_caption("KINGDOM OF FRAUZ 2")

    # Colors
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 170)
    GREEN = (0, 170, 0)
    CYAN = (0, 170, 170)
    RED = (170, 0, 0)
    MAGENTA = (170, 0, 170)
    BROWN = (170, 85, 0)
    LIGHT_GRAY = (170, 170, 170)
    DARK_GRAY = (85, 85, 85)
    LIGHT_BLUE = (85, 85, 255)
    LIGHT_GREEN = (85, 255, 85)
    LIGHT_CYAN = (85, 255, 255)
    LIGHT_RED = (255, 85, 85)
    LIGHT_MAGENTA = (255, 85, 255)
    YELLOW = (255, 255, 85)
    WHITE = (255, 255, 255)

    # Level data
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

    # Create a game instance with a sound player
    sound_player = SoundPlayer()
    game = KrozGameLogic(sound_player)
    
    # Find player position in level
    player_x, player_y = None, None
    for y, line in enumerate(level_1):
        if 'P' in line:
            player_x = line.index('P')
            player_y = y
            break
    
    if player_x is None:
        # Use a default position if no 'P' is found
        player_x, player_y = 20, 12
    
    # Print debug info
    print(f"Grid dimensions: {game.grid_width} x {game.grid_height}")
    print(f"Found player at: {player_x}, {player_y}")
    
    # Initialize playfield with safe bounds
    playfield = [[NULL for x in range(game.grid_width)] for y in range(game.grid_height)]
    
    # Add walls around the border
    for x in range(game.grid_width):
        playfield[0][x] = WALL
        playfield[game.grid_height-1][x] = WALL
    for y in range(game.grid_height):
        playfield[y][0] = WALL
        playfield[y][game.grid_width-1] = WALL
    
    for y, line in enumerate(level_1):
        for x, char in enumerate(line):

            grid_x = x+1
            grid_y = y+1

            if grid_x >= game.grid_width or grid_y >= game.grid_height:
                continue

            if char == '#':
                playfield[grid_y][grid_x] = WALL
            elif char == 'X':
                playfield[grid_y][grid_x] = MBLOCK_ID
            elif char == '1':
                #add slow enemy
                playfield[grid_y][grid_x] = SLOW
                game.add_enemy(SLOW, grid_x, grid_y)
            elif char == '2':
                #add medium enemy
                playfield[grid_y][grid_x] = MEDIUM
                game.add_enemy(MEDIUM, grid_x, grid_y)
            elif char == 'F':
                playfield[grid_y][grid_x] = FAST
                game.add_enemy(FAST, grid_x,grid_y)
            elif char == 'B':
                playfield[grid_y][grid_x] = MBLOCK_ID
                game.b_num += 1
                game.bx[game.b_num] = grid_x
                game.by[game.b_num] = grid_y
            elif char == 'P':
                player_x, player_y = grid_x, grid_y

    # Set the playfield
    game.set_playfield(playfield)
    
    # Initialize player position (adjust to fit within grid)
    print(f"Setting player at position: {player_x}, {player_y}")
    
    if player_x is not None and player_y is not None:
        game.set_player_position(player_x,player_y)
    else:
        game.set_player_position(20, 12)  # Use safe default coordinates
    
    # Main game loop variables
    p_x = (PLAY_WIDTH // 2)
    p_y = (WINDOW_HEIGHT // 2) - 24
    p_width = 8
    p_height = 16
    
    level_draw_x = 8
    level_draw_y = 16
    
    run = True
    clock = pygame.time.Clock()

    frame_counter = 0
    
    while run:
        clock.tick(10)  # Control game speed
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Handle input
        keys = pygame.key.get_pressed()
        moved = False

        old_p_x, old_p_y = p_x, p_y
        
        if keys[pygame.K_LEFT] and p_x > 8:
            if game.process_input('w'):
                p_x -= p_width
                moved = True
        if keys[pygame.K_RIGHT] and p_x < 520 - p_width:
            if game.process_input('e'):
                p_x += p_width
                moved = True
        if keys[pygame.K_UP] and p_y > 16:
            if game.process_input('n'):
                p_y -= p_height
                moved = True
        if keys[pygame.K_DOWN] and p_y < 384 - p_height:
            if game.process_input('s'):
                p_y += p_height
                moved = True

        if moved:
            sound_player.FootStep(game.fast_pc)

        frame_counter += 1
        if frame_counter >= 5:
            frame_counter = 0

            game_state = game.update()
        else:
            game_state = game.get_game_state()
        
        # Check game state
        if game_state['game_over']:
            print("Game over!")
            font = pygame.font.SysFont('Arial', 30)
            game_over_text = font.render("GAME OVER", True, RED)
            window.blit(game_over_text, (WINDOW_WIDTH//2 - 80, WINDOW_HEIGHT//2))
            pygame.display.update()
            pygame.time.delay(2000)
            break
        
        # Drawing
        window.fill(BLACK)
        
        # Draw HUD
        pygame.draw.rect(window, BLUE, (528, 0, 112, 400))
        
        # Draw score and gems in HUD
        font = pygame.font.SysFont('Arial', 16)
        score_text = font.render(f"Score: {game_state['score']}", True, WHITE)
        gems_text = font.render(f"Gems: {game_state['gems']}", True, WHITE)
        window.blit(score_text, (540, 50))
        window.blit(gems_text, (540, 80))
        
        # Draw borders
        pygame.draw.rect(window, GREEN, (520, 0, 8, 400))  # right border
        pygame.draw.rect(window, GREEN, (0, 0, 8, 400))    # left border
        pygame.draw.rect(window, GREEN, (8, 0, 512, 16))   # top border
        pygame.draw.rect(window, GREEN, (8, 384, 512, 16)) # bottom border
        
        # Draw level
        level_draw_x = 8
        level_draw_y = 16
        for line in level_1:
            for element in line:
                if element == 'X':
                    pygame.draw.rect(window, BROWN, (level_draw_x, level_draw_y, 8, 16))
                if element == 'W':
                    pygame.draw.rect(window, WHITE, (level_draw_x, level_draw_y, 8, 16))
                if element == 'L':
                    pygame.draw.rect(window, LIGHT_GRAY, (level_draw_x, level_draw_y, 8, 16))
                if element == 'C':
                    pygame.draw.rect(window, RED, (level_draw_x, level_draw_y, 8, 16))
                if element == '+':
                    pygame.draw.rect(window, GREEN, (level_draw_x, level_draw_y, 8, 16))
                if element == 'T':
                    pygame.draw.rect(window, LIGHT_MAGENTA, (level_draw_x, level_draw_y, 8, 16))
                if element == '#':
                    pygame.draw.rect(window, BROWN, (level_draw_x, level_draw_y, 8, 16))
                level_draw_x += 8
            level_draw_x = 8
            level_draw_y += 16
        level_draw_y = 16
        
        # Draw enemies from game state
        for i in range(1, game.s_num + 1):
            if game.sx[i] is not None:

                enemy_x = (game.sx[i] - 1) * 8  # Adjust for grid/pixel conversion
                enemy_y = (game.sy[i] - 1) * 16      # Adjust for grid/pixel conversion
                pygame.draw.rect(window, LIGHT_RED, (enemy_x, enemy_y, 8, 16))
        
        for i in range(1, game.m_num + 1):
            if game.mx[i] is not None:

                enemy_x = (game.mx[i] - 1) * 8  # Adjust for grid/pixel conversion
                enemy_y = (game.my[i] - 1) * 16      # Adjust for grid/pixel conversion
                pygame.draw.rect(window, LIGHT_GREEN, (enemy_x, enemy_y, 8, 16))
                
        for i in range(1, game.f_num + 1):
            if game.fx[i] is not None:

                enemy_x = (game.fx[i] - 1) * 8  # Adjust for grid/pixel conversion
                enemy_y = (game.fy[i] - 1) * 16      # Adjust for grid/pixel conversion
                pygame.draw.rect(window, LIGHT_BLUE, (enemy_x, enemy_y, 8, 16))
        
        for i in range(1, game.b_num + 1):
            if game.fx[i] is not None:

                block_x = (game.bx[i] - 1) * 8
                block_y = (game.by[i] - 1) * 16
                pygame.draw.rect(window, BROWN, (block_x, block_y, 8, 16))
        # Draw player (either use visual position or game logic position)
        # Using visual position for now
        pygame.draw.rect(window, YELLOW, (p_x, p_y, p_width, p_height))
        
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    run_kroz_game()