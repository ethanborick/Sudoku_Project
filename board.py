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
        self.cells = [[Cell(0, i , j, screen) for j in range(BOARD_COLS)] for i in range(BOARD_ROWS)]
        self.selected_cell = None
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
    def select(self, row, col):
        self.cells[row][col].selected = True
        self.cells[row][col].draw()
        self.selected_cell = self.cells[row][col]
    def click(self, x, y):
        if 0 <= x <= WIDTH and 0 <= y <= HEIGHT:
            row = y // SMALL_SQUARE_SIZE
            col = x // SMALL_SQUARE_SIZE
            return (row, col)
        return None
    def clear(self, row, col):
        if self.cells[row][col].value != 0:
            self.cells[row][col].set_cell_value(0)
    def sketch(self, value):
        if not self.selected_cell.given_value:
            self.selected_cell.set_sketched_value(value)







