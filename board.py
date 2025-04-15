# board class
import pygame, sys
from constants import *
from cell import *
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i , j, screen) for j in range(BOARD_ROWS)] for i in range(BOARD_COLS)]
    def draw(self):
        for i in range(BOARD_ROWS + 1):
            line_thickness = BOLD_LINE_WIDTH if i % 3 == 0 else LINE_WIDTH
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SMALL_SQUARE_SIZE),
                (WIDTH, i * SMALL_SQUARE_SIZE),
                line_thickness
            )

        for i in range(BOARD_COLS + 1):
            line_thickness = BOLD_LINE_WIDTH if i % 3 == 0 else LINE_WIDTH
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SMALL_SQUARE_SIZE, 0),
                (i * SMALL_SQUARE_SIZE, HEIGHT - SMALL_SQUARE_SIZE),
                line_thickness
            )

        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.cells[i][j].draw()



