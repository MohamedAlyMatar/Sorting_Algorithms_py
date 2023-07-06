import pygame
import random
pygame.init()

class DrawInformation:
    # COLORS
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED   = 255, 0, 0
    BLUE  = 0, 0, 255
    GREY  = 128, 128, 128
    BACKGROUND_GREY = WHITE

    # PADDING
    SIDE_PAD = 100
    TOP_PAD  = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Python Sorting Algorithms Visualizer")
        self.set_lst(lst)

    
    def set_lst(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_value - self.max_value))
        self.start_x = self.SIDE_PAD // 2