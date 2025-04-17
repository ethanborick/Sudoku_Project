import pygame, sys
from board import Board
from sudoku_generator import generate_sudoku
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

FONT = pygame.font.Font(None, 40)
BIG_FONT = pygame.font.Font(None, 70)

START, PLAYING, GAMEOVER = "start", "playing", "gameover"

game_state = START
difficulty = None
board = None
buttons = []
buttons_dict = {}
win = False


def init_buttons():
    global buttons_dict
    BUTTON_Y = HEIGHT - 60
    buttons_dict = {
        "reset": pygame.Rect(50, BUTTON_Y, 150, 50),
        "restart": pygame.Rect(260, BUTTON_Y, 150, 50),
        "exit": pygame.Rect(470, BUTTON_Y, 150, 50)
    }


def starting_screen():
    screen.fill((255, 255, 255))
    background = pygame.image.load("background.jpg")
    screen.blit(pygame.transform.scale(background, (WIDTH, HEIGHT)), (0, 0))

    title = pygame.font.Font(None, 80).render("Welcome to Sudoku", True, (0, 0, 0))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 6))

    subtitle = pygame.font.Font(None, 50).render("Select Game Mode:", True, (0, 0, 0))
    screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, HEIGHT // 2 - 50))

    y_pos = HEIGHT * 4 // 6
    difficulties = ["Easy", "Medium", "Hard"]
    rendered_buttons = []

    for i, diff in enumerate(difficulties):
        rect = pygame.Rect(WIDTH // 2 - 240 + i * 160, y_pos, 140, 60)
        pygame.draw.rect(screen, (139, 69, 19), rect, border_radius=5)
        pygame.draw.rect(screen, (255, 255, 255), rect.inflate(-8, -8), border_radius=5)
        pygame.draw.rect(screen, (255, 140, 0), rect.inflate(-16, -16), border_radius=5)

        text = FONT.render(diff.upper(), True, (255, 255, 255))
        screen.blit(text, (
        rect.x + rect.width // 2 - text.get_width() // 2, rect.y + rect.height // 2 - text.get_height() // 2))
        rendered_buttons.append((rect, diff.lower()))

    pygame.display.flip()
    return rendered_buttons


def starting_game_screen(board):
    screen.fill(START_COLOR)
    board.draw()
    drawing_buttons(buttons_dict)
    pygame.display.flip()


def drawing_buttons(buttons_dict):
    for name, rect in buttons_dict.items():
        pygame.draw.rect(screen, (139, 69, 19), rect, border_radius=5)
        pygame.draw.rect(screen, (255, 255, 255), rect.inflate(-8, -8), border_radius=5)
        pygame.draw.rect(screen, (255, 140, 0), rect.inflate(-16, -16), border_radius=5)
        text = FONT.render(name.capitalize(), True, (255, 255, 255))
        screen.blit(text, (
            rect.x + rect.width // 2 - text.get_width() // 2,
            rect.y + rect.height // 2 - text.get_height() // 2
        ))


def ending_game_screen(win):
    screen.fill((255, 255, 255))
    background = pygame.image.load("background.jpg")
    screen.blit(pygame.transform.scale(background, (WIDTH, HEIGHT)), (0, 0))
    msg = "You Win!" if win else "Game Over!"
    result_text = BIG_FONT.render(msg, True, (0, 0, 0))
    screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 3))
    pygame.display.flip()


def creating_board(level):
    removed = 30 if level == "easy" else 40 if level == "medium" else 50
    board_values = generate_sudoku(9, removed)
    b = Board(WIDTH, HEIGHT, screen, level)
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            b.cells[i][j].value = board_values[i][j]
            if board_values[i][j] != 0:
                b.cells[i][j].given_value = True
    return b


def main():
    global game_state, board, difficulty, buttons, win
    clock = pygame.time.Clock()
    init_buttons()
    buttons = starting_screen()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_state == START:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for rect, level in buttons:
                        if rect.collidepoint(pos):
                            difficulty = level
                            board = creating_board(level)
                            game_state = PLAYING

            elif game_state == PLAYING:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for name, rect in buttons_dict.items():
                        if rect.collidepoint(pos):
                            if name == "reset":
                                board.reset_to_original()
                            elif name == "restart":
                                game_state = START
                                buttons = starting_screen()
                            elif name == "exit":
                                pygame.quit()
                                sys.exit()
                    cell_pos = board.click(*pos)
                    if cell_pos:
                        board.select(*cell_pos)

                elif event.type == pygame.KEYDOWN:
                    if board.selected_cell:
                        r, c = board.selected_cell
                        if event.unicode.isdigit() and event.unicode in "123456789":
                            board.sketch(int(event.unicode))
                        elif event.key == pygame.K_RETURN:
                            if board.cells[r][c].sketched_value != 0:
                                board.place_number(board.cells[r][c].sketched_value)
                        elif event.key == pygame.K_BACKSPACE:
                            board.clear()

            if game_state == PLAYING and board:
                if board.is_full():
                    board.update_board()
                    win = board.check_board()
                    game_state = GAMEOVER

        if game_state == START:
            pass
        elif game_state == PLAYING:
            starting_game_screen(board)
        elif game_state == GAMEOVER:
            ending_game_screen(win)
            pygame.time.wait(500)
            game_state = START
            buttons = starting_screen()


if __name__ == "__main__":
    main()
