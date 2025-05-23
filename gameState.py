import random
import time
import numpy as np
import pygame
import os
import pickle
from levelLoader import levelLoader
import sys 
import objectContainer
from screenFunctions import Screen

# constants from original Kroz file
NULL = 0
SLOW = 1
MEDIUM = 2
FAST = 3
WALL = 4
PLAYER_ID = 40
MBLOCK_ID = 38

# Own constants
EWALL = 88
WHIP_PICKUP = 47
TELEPORT_PICKUP = 48
GEM_PICKUP = 49

container = objectContainer.objectContainer()
levelloader = levelLoader(container)

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
        # create stereo audio data by duplicating the mono data
        stereo_audio_data = np.column_stack((audio_data, audio_data))
        # create a sound object
        sound = pygame.sndarray.make_sound(stereo_audio_data)
        sound.play(-1)  # Play indefinitely

    def nosound(self):
        """Stop the sound."""
        pygame.mixer.stop()

    def delay(self, milliseconds):
        time.sleep(milliseconds / 1000)

    def play(self, frequency1, frequency2, delay_length):
        if frequency1 <= frequency2:
            for x in range(frequency1, frequency2 + 1):
                self.sound(x)
                self.delay(delay_length)
        else:
            for x in range(frequency1, frequency2 - 1, -1):  # down to frequency2
                self.sound(x)
                self.delay(delay_length)
        self.nosound()

    def FootStep(self, FastPC):
        for x in range(1, int(FastPC) * 50 + int(not FastPC) * 23):
            self.sound(random.randint(0, 550) + 350)
            self.delay(0.01)  # added delay to compensate for fast CPU
        self.delay(2);  # Added delay to compensate for fast CPU
        self.nosound()
        self.delay(120);
        for x in range(1, int(FastPC) * 60 + int(not FastPC) * 30):
            self.sound(random.randint(0, 50) + 150)
            self.nosound()

    def GrabSound(self, FastPC):
        for x in range(1, int(FastPC) * 160 + int(not FastPC) * 65):
            self.sound(random.randint(0, 1000) + 1000)
            self.delay(0.01)  # added delay to compensate for fast CPU
        self.nosound()

    def BlockSound(self, FastPC):
        for x in range(60, 30, -1):
            self.sound(x)
            self.delay(1 + int(FastPC) * 2)
        self.nosound()

    def NoneSound(self):
        for x in range(1, 5):
            self.sound(400)
            self.delay(10)
            self.nosound()
            self.delay(10);
        self.sound(700)
        self.delay(10)
        self.nosound()
        self.delay(10);

# Whip animation
def animate_whip(window, game, p_x, p_y):
    # Direction-based characters
    direction_chars = {
        (0, -1): '|',  
        (1, -1): '/',  
        (1, 0): '-',   
        (1, 1): '\\',   
        (0, 1): '|',    
        (-1, 1): '/',   
        (-1, 0): '-',   
        (-1, -1): '\\' 
    }
    
    # Directions for the whip animation
    directions = [
        (0, -1),   
        (1, -1),  
        (1, 0),  
        (1, 1),   
        (0, 1),   
        (-1, 1),  
        (-1, 0),  
        (-1, -1)   
    ]
    
    tile_width = 8
    tile_height = 16

    whip_color = (255, 255, 255) 
    
    screen_copy = window.copy()
    
    # Track and clear last known pos
    last_pos = None
    
    # Draw each character in circular sequence
    for dx, dy in directions:
        # Calculate position
        whip_x = p_x + (dx * tile_width)
        whip_y = p_y + (dy * tile_height)
        
        # Clear the previous position by restoring from screen_copy
        if last_pos:
            # Get the rect for the last position
            last_rect = pygame.Rect(last_pos[0], last_pos[1], tile_width, tile_height)
            window.blit(screen_copy, last_rect, last_rect)
            pygame.display.update(last_rect)
        
        # Draw the appropriate character for this direction
        char = direction_chars[(dx, dy)]
        font = pygame.font.SysFont('Arial', 16)
        text = font.render(char, True, whip_color)
        window.blit(text, (whip_x, whip_y))
        
        # Update only the specific part of the display
        pygame.display.update(pygame.Rect(whip_x, whip_y, tile_width, tile_height))
        
        last_pos = (whip_x, whip_y)
        
        pygame.time.delay(20)

    for dx, dy in directions:
        whip_x = p_x + (dx * tile_width)
        whip_y = p_y + (dy * tile_height)
        rect = pygame.Rect(whip_x, whip_y, tile_width, tile_height)
        window.blit(screen_copy, rect, rect)

    pygame.display.update()
    del screen_copy


class KrozGameLogic:
    def __init__(self, sound_player=None, playfield=None):

        container_class = None
        for name in  dir(objectContainer):
            if not name.startswith('__'):
                item = getattr(objectContainer, name)
                if isinstance(item, type):
                    container_class = item
                    break

        if container_class is None:
            if isinstance(objectContainer, type):
                container_class = objectContainer
            else:
                container_class = getattr(objectContainer, objectContainer.__name__, None)

        if container_class:
            container_instance = container_class()
            print(f"Using container class: {container_class.__name__}")
        else:
            print("Could not find container class, creating a minimal compatible object")
            class TempContainer:
                def __init__(self):
                    self.FP = [None] * 24
                    self.PF = [[0 for _ in range(26)] for _ in range(67)]

            container_instance = TempContainer()

        # grid dimensions
        self.grid_width = 80  # original game dimensions
        self.grid_height = 25

        # creates playfield array or use the provided one
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
        self.gems = 20
        self.whips = 10
        self.teleports = 0
        self.keys = 0
        self.whip_power = 1
        self.sideways = False
        self.LevelNumber = 1

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

        #enemy type
        self.s_type = [None] * 100
        self.m_type = [None] * 100
        self.f_type = [None] * 100

        # Timing variables from original
        self.skip_time = 0
        self.fast_pc = True  # Original FastPC variable

        # Set sound player (use the one provided or create a new one)
        self.sound_player = sound_player if sound_player else SoundPlayer()

        # Game state flag
        self.game_over = False
        self.level_complete = False

    def load_level(self, level_number=None):
        """Load a specific level or the current level if none specified"""
        if level_number is not None:
            self.LevelNumber = level_number
    
        # Check if level_loader is available
        if self.level_loader:
            print(f"Loading level {self.LevelNumber} using level loader")
            try:
                # Try to use the level loader
                self.level_loader.Level(self.LevelNumber)
            
            # Try to get the player position
                try:
                    if hasattr(self.level_loader.objectContainer, 'PX') and hasattr(self.level_loader.objectContainer, 'PY'):
                        self.set_player_position(
                            self.level_loader.objectContainer.PX, 
                            self.level_loader.objectContainer.PY
                        )
                        print(f"Player position set to {self.px}, {self.py}")
                    else:
                        print("Player position not found in level loader, using default")
                except Exception as e:
                    print(f"Error getting player position: {e}")
                
                # Try to get playfield data
                try:
                    if hasattr(self.level_loader.objectContainer, 'PF'):
                        self.pf = self.level_loader.objectContainer.PF
                        print("Playfield data loaded from level loader")
                    else:
                        print("Playfield data not found in level loader, using default")
                except Exception as e:
                    print(f"Error getting playfield data: {e}")
                
                return True
                
            except Exception as e:
                print(f"Error loading level: {e}")
                # Fallback to basic level
                return self._load_fallback_level()
        else:
            print("Level loader not available, using fallback level")
            return self._load_fallback_level()

    def _load_fallback_level(self):
        """Load a basic level in case the level loader fails"""
        print("Loading fallback level")
        # Create a simple level with walls around the border
        for x in range(self.grid_width):
            self.pf[0][x] = WALL
            self.pf[self.grid_height-1][x] = WALL
        for y in range(self.grid_height):
            self.pf[y][0] = WALL
            self.pf[y][self.grid_width-1] = WALL
    
        # Set player position
        self.set_player_position(self.grid_width // 2, self.grid_height // 2)
    
        # Add a few enemies for testing
        self.add_enemy(SLOW, 10, 10, '1')
        self.add_enemy(MEDIUM, 30, 15, '1')
        self.add_enemy(FAST, 50, 5, '1')
    
        return True
    
    def next_level(self):
        """Progress to the next level based on levelLoader's progression"""
        if self.LevelNumber == 1:
            self.LevelNumber = 2
        elif self.LevelNumber == 2:
            self.LevelNumber = 4
        elif self.LevelNumber == 4:
            self.LevelNumber = 6
        elif self.LevelNumber == 6:
            self.LevelNumber = 8
        elif self.LevelNumber == 8:
            self.LevelNumber = 10
        elif self.LevelNumber == 10:
            self.LevelNumber = 12
        elif self.LevelNumber == 12:
            self.LevelNumber = 14
        elif self.LevelNumber == 14:
            self.LevelNumber = 16
        elif self.LevelNumber == 16:
            self.LevelNumber = 18
        elif self.LevelNumber == 18:
            self.LevelNumber = 20
        elif self.LevelNumber == 20:
            self.LevelNumber = 22
        elif self.LevelNumber == 22:
            self.LevelNumber = 24
        elif self.LevelNumber == 24:
            self.LevelNumber = 25
        else:
            # Game complete or invalid level
            self.game_over = True
            return self.get_game_state()
    
        # Load the new level
        self.level_loader.Level(self.LevelNumber)
    
        # Set level complete flag to false
        self.level_complete = False
    
        # Transfer level data from level_loader to game state
        # This might vary based on how your code is structured
        # For example:
        self.pf = self.level_loader.objectContainer.PF
    
        # Update player position
        if hasattr(self.level_loader.objectContainer, 'PX') and hasattr(self.level_loader.objectContainer, 'PY'):
            self.set_player_position(self.level_loader.objectContainer.PX, self.level_loader.objectContainer.PY)
    


        # Return full game state
        return self.get_game_state()

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

    def add_enemy(self, enemy_type, x, y, num):
        """Add an enemy at a specific position"""
        # Make sure x and y are within valid range
        if not (0 <= x < self.grid_width and 0 <= y < self.grid_height):
            return

        if enemy_type == SLOW:
            self.s_num += 1
            self.sx[self.s_num] = x
            self.sy[self.s_num] = y
            self.pf[y][x] = SLOW
            self.s_type[self.s_num] = num
        elif enemy_type == MEDIUM:
            self.m_num += 1
            self.mx[self.m_num] = x
            self.my[self.m_num] = y
            self.pf[y][x] = MEDIUM
            self.m_type[self.m_num] = num
        elif enemy_type == FAST:
            self.f_num += 1
            self.fx[self.f_num] = x
            self.fy[self.f_num] = y
            self.pf[y][x] = FAST
            self.f_type[self.f_num] = num


    def move(self, dx, dy):
        """Direct port of original move procedure with collectible handling"""
        new_x = self.px + dx
        new_y = self.py + dy

        # Check bounds (matching original)
        if (new_x < 1 or new_x >= self.grid_width - 1 or
                new_y < 1 or new_y >= self.grid_height - 1):
            return False

        new_pos_value = self.pf[new_y][new_x]

        # Original walkable tiles + collectibles
        if new_pos_value in [NULL, 32, 33, 37, 39, 41, 44, 47, 48, 49, 50]:
            # Check if this is a collectible
            if new_pos_value == WHIP_PICKUP:
                self.whips += 1
                new_pos_value = NULL  
                
                grid_x = new_x - 1  
                grid_y = new_y - 1
                if 0 <= grid_y < len(levelloader.objectContainer.FP) and grid_x < len(levelloader.objectContainer.FP[grid_y]):
                    line = list(levelloader.objectContainer.FP[grid_y])
                    line[grid_x] = ' ' 
                    levelloader.objectContainer.FP[grid_y] = ''.join(line)
            
            elif new_pos_value == TELEPORT_PICKUP:
                self.teleports += 1 
                new_pos_value = NULL  
                
                grid_x = new_x - 1  
                grid_y = new_y - 1
                if 0 <= grid_y < len(levelloader.objectContainer.FP) and grid_x < len(levelloader.objectContainer.FP[grid_y]):
                    line = list(levelloader.objectContainer.FP[grid_y])
                    line[grid_x] = ' ' 
                    levelloader.objectContainer.FP[grid_y] = ''.join(line)

            elif new_pos_value == GEM_PICKUP:
                self.gems += 1
                self.score += 5 
                new_pos_value = NULL  
                
                grid_x = new_x - 1 
                grid_y = new_y - 1
                if 0 <= grid_y < len(levelloader.objectContainer.FP) and grid_x < len(levelloader.objectContainer.FP[grid_y]):
                    line = list(levelloader.objectContainer.FP[grid_y])
                    line[grid_x] = ' '
                    levelloader.objectContainer.FP[grid_y] = ''.join(line)

            # Handle replacement like original
            if self.replacement is not None:
                self.pf[self.py][self.px] = self.replacement
            else:
                self.pf[self.py][self.px] = NULL

            self.px = new_x
            self.py = new_y
            self.replacement = new_pos_value  # Store the replacement (which might be NULL now for collectibles)
            self.pf[new_y][new_x] = PLAYER_ID
            return True

        # Wall or other obstacle
        return False

    def use_whip(self):
        if self.whips < 1:
            return False

        self.whips -= 1

        # Check all 8 directions around player and hit what's there
        directions = [
            (-1, -1), (-1, 0), (-1, 1), 
            (0, -1), (0, 1), 
            (1, -1), (1, 0), (1, 1)  
        ]

        for dx, dy in directions:
            x, y = self.px + dx, self.py + dy
            # check bounds
            if 0 <= x < self.grid_width and 0 <= y < self.grid_height:
                # Check what's at this position and handle it
                target_tile = self.pf[y][x]
                
                if target_tile == EWALL or target_tile == MBLOCK_ID:
                    # Destroy walls or blocks
                    self.pf[y][x] = NULL
                    
                    # Also update the level data
                    grid_x = x - 1  # Convert to level data coordinates
                    grid_y = y - 1
                    if 0 <= grid_y < len(levelloader.objectContainer.FP) and grid_x < len(levelloader.objectContainer.FP[grid_y]):
                        line = list(levelloader.objectContainer.FP[grid_y])
                        line[grid_x] = ' '  
                        levelloader.objectContainer.FP[grid_y] = ''.join(line)
                    
                    if target_tile == MBLOCK_ID:
                        for i in range(1, self.b_num + 1):
                            if self.bx[i] == x and self.by[i] == y:
                                self.bx[i] = None
                                break
                elif target_tile in [SLOW, MEDIUM, FAST]:
                    self.pf[y][x] = NULL
                    
                    grid_x = x - 1
                    grid_y = y - 1
                    if 0 <= grid_y < len(levelloader.objectContainer.FP) and grid_x < len(levelloader.objectContainer.FP[grid_y]):
                        line = list(levelloader.objectContainer.FP[grid_y])
                        line[grid_x] = ' '
                        levelloader.objectContainer.FP[grid_y] = ''.join(line)
                    if target_tile == SLOW:
                        for i in range(1, self.s_num + 1):
                            if self.sx[i] == x and self.sy[i] == y:
                                self.sx[i] = None
                                self.score += 1
                                break
                    elif target_tile == MEDIUM:
                        for i in range(1, self.m_num + 1):
                            if self.mx[i] == x and self.my[i] == y:
                                self.mx[i] = None
                                self.score += 2
                                break
                    elif target_tile == FAST:
                        for i in range(1, self.f_num + 1):
                            if self.fx[i] == x and self.fy[i] == y:
                                self.fx[i] = None
                                self.score += 3
                                break
        return True

    def use_teleport(self):
        """Implements the teleport action from the original game"""
        if self.teleports < 1:
            return False

        self.teleports -= 1

        # visual effects for teleportation
        for x in range(250):
            self.sound_player.sound(random.randint(20, 40))

        # clear player from current position
        self.pf[self.py][self.px] = self.replacement
        self.replacement = NULL

        # Find a valid teleport destination
        found_spot = False
        while not found_spot:
            new_x = random.randint(1, 64)
            new_y = random.randint(1, 24)

            if self.pf[new_y][new_x] == NULL:
                self.px = new_x
                self.py = new_y
                self.pf[new_y][new_x] = PLAYER_ID
                found_spot = True
                
        return True

    def use_key(self, x, y):
        """Try to use a key at the specified position"""
        if self.keys < 1:
            self.sound_player.NoneSound()
            return False

        # check if there's a lock at the specified location
        # you need to define what tile ID represents a lock
        LOCK_ID = 13

        if 0 <= x < self.grid_width and 0 <= y < self.grid_height:
            if self.pf[y][x] == LOCK_ID:
                self.keys -= 1
                self.pf[y][x] = NULL  # Open the lock
                self.sound_player.play(500, 300, 50)  # Play opening sound
                return True

        return False

    def process_input(self, direction):
        """
        Process player movement and actions based on input
        direction should be one of: 'n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', ' whip', 'teleport'
        """
        if direction == 'whip':
            return self.use_whip()
        elif direction == 'teleport':
            return self.use_teleport()
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
                if self.s_type[loop] == '1':
                    self.gems -= 1
                elif self.s_type[loop] == '2':
                    self.gems -= 2

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
                if self.m_type[loop] == '1':
                    self.gems -= 1
                elif self.m_type[loop] == '2':
                    self.gems -= 2

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
                if self.f_type[loop] == '1':
                    self.gems -= 1
                elif self.f_type[loop] == '2':
                    self.gems -= 2

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

        # Return full game state
        return self.get_game_state()

    def get_game_state(self):
        """Return the current game state for rendering"""
        return {
            'playfield': self.pf,
            'player_x': self.px,
            'player_y': self.py,
            'score': self.score,
            'gems': self.gems,
            'whips': self.whips,
            'teleports': self.teleports,
            'keys': self.keys,
            'whip_power': self.whip_power,
            'game_over': self.game_over,
            'level_complete': self.level_complete
        }

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Add save game function
def save_game(game, current_level, p_x, p_y):
    """Save the current game state to a file"""
    save_data = {
        'game_state': game.get_game_state(),
        'current_level': current_level,
        'player_visual_x': p_x,
        'player_visual_y': p_y,
        'slow_enemies': [(game.sx[i], game.sy[i]) for i in range(1, game.s_num + 1) if game.sx[i] is not None],
        'medium_enemies': [(game.mx[i], game.my[i]) for i in range(1, game.m_num + 1) if game.mx[i] is not None],
        'fast_enemies': [(game.fx[i], game.fy[i]) for i in range(1, game.f_num + 1) if game.fx[i] is not None],
        'moving_blocks': [(game.bx[i], game.by[i]) for i in range(1, game.b_num + 1) if game.bx[i] is not None],
        's_num': game.s_num,
        'm_num': game.m_num,
        'f_num': game.f_num,
        'b_num': game.b_num
    }

    # Create saves directory if it doesn't exist
    if not os.path.exists('saves'):
        os.makedirs('saves')

    # Save to file
    with open('saves/kroz_save.dat', 'wb') as f:
        pickle.dump(save_data, f)

    print("Game saved successfully!")
    return True


def run_kroz_game(current_level=1, load_save=False):
    """
    Run the Kroz game with enemy progression based on level number
    - Level 1-4: Only slow enemies
    - Level 5-9: Slow and medium enemies
    - Level 10-14: Slow and fast enemies
    - Level 15+: Slow, fast, and wall enemies
    """
    pygame.init()
    pygame.font.init()

    # Set up the window and display
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 400
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    PLAY_WIDTH = 512
    PLAY_HEIGHT = 370

    pygame.display.set_caption("KINGDOM OF FRAUZ 2 - LEVEL {current_level}")

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

    levelloader.objectContainer.screen = Screen()

    levelloader.Init_Screen()
    levelloader.Level(1)
    levelloader.Display_Playfield()

    # Create a game instance with a sound player
    sound_player = SoundPlayer()
    game = KrozGameLogic(sound_player)

    # try to load saved game if requested
    p_x = (PLAY_WIDTH // 2)
    p_y = (WINDOW_HEIGHT // 2) - 24

    if load_save and os.path.exists('saves/kroz_save.dat'):
        try:
            with open('saves/kroz_save.dat', 'rb') as f:
                save_data = pickle.load(f)

            # Load game state
            current_level = save_data['current_level']
            p_x = save_data['player_visual_x']
            p_y = save_data['player_visual_y']

            print(f"Game loaded! Resuming level {current_level}")
        except Exception as e:
            print(f"Error loading saved game: {e}")
            # Continue with a new game

    # Find player position in level
    player_x, player_y = None, None
    for y in range(1, len(levelloader.objectContainer.FP) - 1):  # Start from 1
        line = levelloader.objectContainer.FP[y]  # Access the line using 0-based index
        if 'P' in line:
            player_x = line.index('P')       # Convert to 1-based index
            player_y = y                     # Already 1-based
            break

    if player_x is None:
        # Use a default position if no 'P' is found
        player_x, player_y = 20, 12

    # Print debug info
    print(f"Grid dimensions: {game.grid_width} x {game.grid_height}")
    print(f"Found player at: {player_x}, {player_y}")
    print(f"Current Level: {current_level}")

    # Initialize playfield with safe bounds
    playfield = [[NULL for x in range(game.grid_width)] for y in range(game.grid_height)]

    # Add walls around the border
    for x in range(game.grid_width):
        playfield[0][x] = WALL
        playfield[game.grid_height - 1][x] = WALL
    for y in range(game.grid_height):
        playfield[y][0] = WALL
        playfield[y][game.grid_width - 1] = WALL

    # Process level data with enemy progression based on current level
    for y in range(1, len(levelloader.objectContainer.FP) - 1):
        for x, char in enumerate(levelloader.objectContainer.FP[y]):
            grid_x = x + 1
            grid_y = y + 1

            if grid_x >= game.grid_width or grid_y >= game.grid_height:
                continue

            if char == '#':
                playfield[grid_y][grid_x] = WALL
            elif char == 'X':
                playfield[grid_y][grid_x] = MBLOCK_ID
            elif char in ['1', '2', 'F']:  # Add enemy character
                # Determine which enemy type to use based on level
                if current_level < 5:
                    # levels 1-4: slow enemies
                    playfield[grid_y][grid_x] = SLOW
                    game.add_enemy(SLOW, grid_x, grid_y, char)
                elif 5 <= current_level < 10:
                    # replace slow with medium enemy
                    playfield[grid_y][grid_x] = MEDIUM
                    game.add_enemy(MEDIUM, grid_x, grid_y, char)
                else:
                    # levels 10+: all enemies are fast
                    playfield[grid_y][grid_x] = FAST
                    game.add_enemy(FAST, grid_x, grid_y, char)
            elif char == "$":
                if current_level < 15:
                    # level 1-14: wall enemies are normal walls
                    playfield[grid_y][grid_x] = WALL
                else:
                    # level 15+: Add moving wall enemies
                    playfield[grid_y][grid_x] = MBLOCK_ID
                    game.b_num += 1
                    game.bx[game.b_num] = grid_x
                    game.by[game.b_num] = grid_y
            elif char == 'B':
                if current_level < 15:
                    # levels 1-14: normal walls for moving blocks
                    playfield[grid_y][grid_x] = WALL
                else:
                    # level 15+ : add moving blocks
                    playfield[grid_y][grid_x] = MBLOCK_ID
                    game.b_num += 1
                    game.bx[game.b_num] = grid_x
                    game.by[game.b_num] = grid_y
            elif char == 'P':
                player_x, player_y = grid_x, grid_y
            elif char == 'W':  # Whip pickup
                playfield[grid_y][grid_x] = WHIP_PICKUP
            elif char == 'T':  # Teleport pickup
                playfield[grid_y][grid_x] = TELEPORT_PICKUP
            elif char == '+':  # Gem pickup
                playfield[grid_y][grid_x] = GEM_PICKUP


    # Set the playfield
    game.set_playfield(playfield)

    # Initialize player position (adjust to fit within grid)
    print(f"Setting player at position: {player_x}, {player_y}")

    if player_x is not None and player_y is not None:
        game.set_player_position(player_x, player_y)
    else:
        game.set_player_position(20, 12)  # Use safe default coordinates

    # Main game loop variables
    p_width = 8
    p_height = 16

    level_draw_x = 8
    level_draw_y = 16

    run = True
    clock = pygame.time.Clock()
    frame_counter = 0
    paused = False
    saved_message_timer = 0

    # Define the sidebar drawing function
    def draw_sidebar(window, game_state, current_level, saved_message=False):
        """Draw the sidebar UI matching the reference image style with gray boxes for values"""
        # Colors
        BLACK = (0, 0, 0)
        BLUE = (0, 0, 170)
        WHITE = (255, 255, 255)
        YELLOW = (255, 255, 85)
        LIGHT_GRAY = (170, 170, 170)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)

        # Draw sidebar background
        pygame.draw.rect(window, BLUE, (528, 0, 112, 400))

        # Font setup
        title_font = pygame.font.SysFont('Arial', 14)
        value_font = pygame.font.SysFont('Arial', 14)
        option_font = pygame.font.SysFont('Arial', 14)
        bold_font = pygame.font.SysFont('Arial', 14, bold=True)

        # Vertical position tracking
        y_pos = 20
        box_height = 20
        box_spacing = 22  # Space between boxes

        # Draw Score with gray box
        score_text = title_font.render("Score", True, WHITE)
        window.blit(score_text, (540, y_pos))
        y_pos += 24

        # Draw score value box
        pygame.draw.rect(window, LIGHT_GRAY, (540, y_pos, 80, box_height))
        score_value = value_font.render(str(game_state['score']), True, BLACK)
        window.blit(score_value, (560, y_pos + 4))  # Center text in box
        y_pos += box_spacing

        # Draw Level with gray box
        level_text = title_font.render("Level", True, WHITE)
        window.blit(level_text, (540, y_pos))
        y_pos += 24

        # Draw level value box
        pygame.draw.rect(window, LIGHT_GRAY, (540, y_pos, 80, box_height))
        level_value = value_font.render(str(current_level), True, BLACK)
        window.blit(level_value, (560, y_pos + 4))
        y_pos += box_spacing

        # Draw Gems with gray box
        gems_text = title_font.render("Gems", True, WHITE)
        window.blit(gems_text, (540, y_pos))
        y_pos += 24

        # Draw gems value box
        pygame.draw.rect(window, LIGHT_GRAY, (540, y_pos, 80, box_height))
        gems_value = value_font.render(str(game_state['gems']), True, BLACK)
        window.blit(gems_value, (560, y_pos + 4))
        y_pos += box_spacing

        # Draw Whips with gray box
        whips_text = title_font.render("Whips", True, WHITE)
        window.blit(whips_text, (540, y_pos))
        y_pos += 24

        # Draw whips value box
        pygame.draw.rect(window, LIGHT_GRAY, (540, y_pos, 80, box_height))
        whips_value = value_font.render(str(game_state['whips']), True, BLACK)
        window.blit(whips_value, (560, y_pos + 4))
        y_pos += box_spacing

        # Draw Teleports with gray box
        teleports_text = title_font.render("Teleports", True, WHITE)
        window.blit(teleports_text, (540, y_pos))
        y_pos += 24

        # Draw teleports value box
        pygame.draw.rect(window, LIGHT_GRAY, (540, y_pos, 80, box_height))
        teleports_value = value_font.render(str(game_state['teleports']), True, BLACK)
        window.blit(teleports_value, (560, y_pos + 4))
        y_pos += box_spacing

        # Draw Keys with gray box
        keys_text = title_font.render("Keys", True, WHITE)
        window.blit(keys_text, (540, y_pos))
        y_pos += 24

        # Draw keys value box
        pygame.draw.rect(window, LIGHT_GRAY, (540, y_pos, 80, box_height))
        keys_value = value_font.render(str(game_state['keys']), True, BLACK)
        window.blit(keys_value, (560, y_pos + 4))
        y_pos += box_spacing + 10

        # Draw OPTIONS header in red
        options_text = title_font.render("OPTIONS", True, RED)
        window.blit(options_text, (540, y_pos))
        y_pos += 24

        # Draw options with first letter in bold to indicate keyboard shortcuts
        options = ["Whip", "Teleport", "Pause", "Quit", "Save"]
        for option in options:
            # render first letter in bold
            first_letter = bold_font.render(option[0], True, WHITE)
            # render the rest of the world in regular font
            rest_of_word = option_font.render(option[1:], True, WHITE)

            # blit the first letter
            window.blit(first_letter, (540, y_pos))

            # Blit the rest of the word (position based on the width of first letter)
            first_letter_width = bold_font.size(option[0])[0]
            window.blit(rest_of_word, (540 + first_letter_width, y_pos))

            y_pos += 13

        # show "Game Saved!" message if recently saved
        if saved_message:
            saved_text = bold_font.render("Game Saved!", True, GREEN)
            window.blit(saved_text, (540, y_pos + 10))

    font_path = resource_path("PerfectDOSVGA437.ttf")
    kroz_font = pygame.font.Font(font_path, 16)
    while run:
        clock.tick(10)  # Control game speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Handle key press events (for single press actions like P, Q, S)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # P for pause
                    paused = not paused
                    print("Game " + ("paused" if paused else "resumed"))

                if event.key == pygame.K_q:  # Q for quit
                    run = False

                if event.key == pygame.K_s:  # S for save
                    if save_game(game, current_level, p_x, p_y):
                        saved_message_timer = 30  # Show message for ~3 seconds

        # handle continuous input (for movement and actions
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

        # update game state less frequently to control speed
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
            window.blit(game_over_text, (WINDOW_WIDTH // 2 - 80, WINDOW_HEIGHT // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            break

        if game_state['level_complete']:
            # Progress to next level
            game_state = game.next_level()
            print(f"Level {current_level} completed! Moving to level {game.LevelNumber}")
            
            current_level = game.LevelNumber
            
            pygame.display.update()
            pygame.time.delay(1000)

        if keys[pygame.K_w]:  # W for whip
            if game.whips > 0:  # Check if whips are available
                if game.use_whip():
                        animate_whip(window,game, p_x, p_y)
                        pygame.display.update()
                pygame.time.delay(100)  

        if keys[pygame.K_t]:  # T for teleport
            if game.use_teleport():
                p_x = (game.px - 1) * 8 + 8
                p_y = (game.py - 1) * 16 + 16

        # Drawing
        window.fill(BLACK)

        # Draw borders
        pygame.draw.rect(window, GREEN, (520, 0, 8, 400))  # right border
        pygame.draw.rect(window, GREEN, (0, 0, 8, 400))  # left border
        pygame.draw.rect(window, GREEN, (8, 0, 512, 16))  # top border
        pygame.draw.rect(window, GREEN, (8, 384, 512, 16))  # bottom border

        # Draw level

        level_draw_x = 8
        level_draw_y = 16
        for y in range(1, len(levelloader.objectContainer.FP) - 1):
            for element in levelloader.objectContainer.FP[y]:
                # TODO: add proper characters
                if element == 'X':
                    window.blit(kroz_font.render("²", False, BROWN), (level_draw_x, level_draw_y))
                if element == 'W':
                    window.blit(kroz_font.render("ô", False, WHITE), (level_draw_x, level_draw_y))
                if element == 'E':
                    window.blit(kroz_font.render("±", False, LIGHT_RED), (level_draw_x, level_draw_y))
                if element == 'L':
                    pygame.draw.rect(window, LIGHT_GRAY, (level_draw_x, level_draw_y, 8, 16))
                    window.blit(kroz_font.render("ð", False, BLACK), (level_draw_x, level_draw_y))
                if element == 'C':
                    pygame.draw.rect(window, RED, (level_draw_x, level_draw_y, 8, 16))
                    window.blit(kroz_font.render("C", False, YELLOW), (level_draw_x, level_draw_y))
                if element == '+':
                    window.blit(kroz_font.render("", False, GREEN), (level_draw_x, level_draw_y))
                if element == 'T':
                    window.blit(kroz_font.render("", False, LIGHT_MAGENTA), (level_draw_x, level_draw_y))
                if element == '#':
                    window.blit(kroz_font.render("Û", False, BROWN), (level_draw_x, level_draw_y))
                level_draw_x += 8
            level_draw_x = 8
            level_draw_y += 16
        level_draw_y = 16

        # Draw enemies from game state
        for i in range(1, game.s_num + 1):
            if game.sx[i] is not None:
                enemy_x = (game.sx[i] - 1) * 8 + 8  # Adjust for grid/pixel conversion
                enemy_y = (game.sy[i] - 1) * 16 + 16  # Adjust for grid/pixel conversion
                if game.s_type[i] == '1':
                    pygame.draw.rect(window, BLACK, (enemy_x, enemy_y, 8, 16))
                    window.blit(kroz_font.render("", False, LIGHT_RED), (enemy_x, enemy_y))
                elif game.s_type[i] == '2':
                    pygame.draw.rect(window, BLACK, (enemy_x, enemy_y, 8, 16))
                    window.blit(kroz_font.render("™", False, LIGHT_GREEN), (enemy_x, enemy_y))

        for i in range(1, game.m_num + 1):
            if game.mx[i] is not None:
                enemy_x = (game.mx[i] - 1) * 8 + 8  # Adjust for grid/pixel conversion
                enemy_y = (game.my[i] - 1) * 16 + 16  # Adjust for grid/pixel conversion
                if game.m_type[i] == '1':
                    pygame.draw.rect(window, BLACK, (enemy_x, enemy_y, 8, 16))
                    window.blit(kroz_font.render("", False, LIGHT_RED), (enemy_x, enemy_y))
                elif game.m_type[i] == '2':
                    pygame.draw.rect(window, BLACK, (enemy_x, enemy_y, 8, 16))
                    window.blit(kroz_font.render("™", False, LIGHT_GREEN), (enemy_x, enemy_y))


        for i in range(1, game.f_num + 1):
            if game.fx[i] is not None:
                enemy_x = (game.fx[i] - 1) * 8 + 8  # Adjust for grid/pixel conversion
                enemy_y = (game.fy[i] - 1) * 16 + 16  # Adjust for grid/pixel conversion
                if game.f_type[i] == '1':
                    pygame.draw.rect(window, BLACK, (enemy_x, enemy_y, 8, 16))
                    window.blit(kroz_font.render("", False, LIGHT_RED), (enemy_x, enemy_y))
                elif game.f_type[i] == '2':
                    pygame.draw.rect(window, BLACK, (enemy_x, enemy_y, 8, 16))
                    window.blit(kroz_font.render("™", False, LIGHT_GREEN), (enemy_x, enemy_y))

        for i in range(1, game.b_num + 1):
            if game.bx[i] is not None:
                block_x = (game.bx[i] - 1) * 8 + 8
                block_y = (game.by[i] - 1) * 16 + 16
                pygame.draw.rect(window, WHITE, (block_x, block_y, 8, 16))
        # Draw player (either use visual position or game logic position)
        # Using visual position for now
        pygame.draw.rect(window, BLACK, (p_x, p_y, 8, 16))
        window.blit(kroz_font.render("", False, YELLOW), (p_x, p_y))

        draw_sidebar(window, game_state, current_level, saved_message_timer > 0)

        pygame.display.update()

    pygame.quit()


def test_level(level_number):
    """Test the game with a specific level number"""
    run_kroz_game(level_number)


if __name__ == "__main__":
    run_kroz_game(1)
