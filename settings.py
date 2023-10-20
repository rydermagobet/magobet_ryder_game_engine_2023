# This file was created by: Ryder Magobet



# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30
SCORE = 0

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5

# define colors
GOLD = (255, 170, 51)
BLACK = (0, 0, 0)
RED = (222, 49, 99)
QUARTS = (112, 41, 99)
BLUE = (0, 0, 255)
JUNGLEGREEN = (42, 170, 138)

# Starting playforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, " "),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, "moving"),
                 (125, HEIGHT - 250, 100, 20, "moving"),
                 (250, 280, 100, 20, "moving"),
                 (175, 100, 50, 20, " "),
                 (75, 50, 25, 20, " "),
                 (125, 150, 15, 10, "moving"),]
                