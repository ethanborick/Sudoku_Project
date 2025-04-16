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
        self.board_values = [[0 for i in range(BOARD_COLS)] for j in range(BOARD_ROWS)]
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
        if not (0 <= row < 9 and 0 <= col < 9):
            print(f"WARNING: Tried to select invalid cell ({row}, {col})")
            return

        if self.selected_cell:
            self.selected_cell.selected = False
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
    def place_number(self, value):
        if self.selected_cell and not self.selected_cell.given_value:
            self.selected_cell.set_cell_value(value)
            self.selected_cell.selected = False
            self.selected_cell = None
    def reset_to_original(self):
        self.selected_cell = None
        for row in self.cells:
            for cell in row:
                if not cell.given_value:
                    cell.sketched_value = 0
                    cell.value = 0
    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True
    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.board_values[i][j] = self.cells[i][j].value
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return (i, j)

    def check_board(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0 and cell.sketched_value != 0:
                    cell.value = cell.sketched_value

        self.update_board()
        for i, row in enumerate(self.board_values):
            if sorted(row) != list(range(1, 10)):
                print(f"[ROW FAIL] Row {i} = {row}")
                return False

        for col in range(9):
            column = [self.board_values[row][col] for row in range(9)]
            if sorted(column) != list(range(1, 10)):
                print(f"[COL FAIL] Column {col} = {column}")
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(self.board_values[box_row + i][box_col + j])
                if sorted(box) != list(range(1, 10)):
                    print(f"[BOX FAIL] Box starting at ({box_row},{box_col}) = {box}")
                    return False

        return True