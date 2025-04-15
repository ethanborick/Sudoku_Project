# cell class
import pygame
from constants import *
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
    def set_cell_value(self, value):
        self.value = value
    def set_sketched_value(self, value):
        self.sketched_value = value
        sketch_font = pygame.font.Font(None, SKETCH_FONT)
        sketch_surf = sketch_font.render(str(value), 0, SKETCH_COLOR)
        sketch_rect = sketch_surf.get_rect(
            center=(
                self.col * SMALL_SQUARE_SIZE + SMALL_SQUARE_SIZE // 2,
                self.row * SMALL_SQUARE_SIZE + SMALL_SQUARE_SIZE // 2
            )
        )
        self.screen.blit(sketch_surf, sketch_rect)
    def draw(self):
        if self.value != 0:
            final_value_font = pygame.font.Font(None, FINAL_VALUE_FONT)
            final_value_surf = final_value_font.render(str(self.value), 0, )
            final_value_rect = final_value_surf.get_rect(
                center = (
                    self.col * SMALL_SQUARE_SIZE + SMALL_SQUARE_SIZE // 2,
                    self.row * SMALL_SQUARE_SIZE + SMALL_SQUARE_SIZE // 2
                )
            )
            self.screen.blit(final_value_surf, final_value_rect)
