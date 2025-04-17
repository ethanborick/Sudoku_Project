# main method
import pygame, sys
from constants import *
from board import *
from cell import *
from sudoku_generator import *

def welcome_to_sudoku(screen):
    title_font = pygame.font.Font(None, 100)
    title_surf = title_font.render("Welcome to Sudoku", 0, (0, 0, 0))
    title_rect = title_surf.get_rect(center = (WIDTH // 2, 150))
    screen.blit(title_surf, title_rect)

    select_game_mode_font = pygame.font.Font(None, 50)
    select_game_mode_surf = select_game_mode_font.render("Select Game Mode:", 0, (0, 0, 0))
    select_game_mode_rect = select_game_mode_surf.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(select_game_mode_surf, select_game_mode_rect)

    easy_font = pygame.font.Font(None, 35)
    easy_surf = easy_font.render("Easy", 0, (255, 255, 255))
    easy_rect = easy_surf.get_rect(center = (WIDTH // 4, 500))
    pygame.draw.rect(screen, (255, 165, 0), easy_rect.inflate(20, 10))
    screen.blit(easy_surf, easy_rect)

    medium_font = pygame.font.Font(None, 35)
    medium_surf = medium_font.render("Medium", 0, (255, 255, 255))
    medium_rect = medium_surf.get_rect(center=(WIDTH // 2, 500))
    pygame.draw.rect(screen, (255, 165, 0), medium_rect.inflate(20, 10))
    screen.blit(medium_surf, medium_rect)

    hard_font = pygame.font.Font(None, 35)
    hard_surf = hard_font.render("Hard", 0, (255, 255, 255))
    hard_rect = hard_surf.get_rect(center=(3 * WIDTH // 4, 500))
    pygame.draw.rect(screen, (255, 165, 0), hard_rect.inflate(20, 10))
    screen.blit(hard_surf, hard_rect)

def get_difficulty(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 131 <= x <= 206 and 483 <= y <= 518: # these are the easy rectangle coords
                    return "Easy"
                if 281 <= x <= 393 and 483 <= y <= 517: # medium rectangle coords
                    return "Medium"
                if 468 <= x <= 545 and 483 <= y <= 517: # hard rectangle coords
                    return "Hard"



