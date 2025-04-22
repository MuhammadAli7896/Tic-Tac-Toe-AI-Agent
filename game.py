import pygame
import sys
import time
from board import Board
from minimax_agent import MinimaxAgent
from alphabeta_agent import AlphaBetaAgent

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
TEXT_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

board = Board()
use_alpha_beta = True  
agent = AlphaBetaAgent('O') if use_alpha_beta else MinimaxAgent('O')
player_turn = True  

font = pygame.font.SysFont('Arial', 32)


def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen, LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )

    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen, LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board.board[row][col] == 'X':
                pygame.draw.line(
                    screen, X_COLOR,
                    (col * SQUARE_SIZE + SQUARE_SIZE * 0.2,
                     row * SQUARE_SIZE + SQUARE_SIZE * 0.2),
                    (col * SQUARE_SIZE + SQUARE_SIZE * 0.8,
                     row * SQUARE_SIZE + SQUARE_SIZE * 0.8),
                    LINE_WIDTH
                )
                pygame.draw.line(
                    screen, X_COLOR,
                    (col * SQUARE_SIZE + SQUARE_SIZE * 0.8,
                     row * SQUARE_SIZE + SQUARE_SIZE * 0.2),
                    (col * SQUARE_SIZE + SQUARE_SIZE * 0.2,
                     row * SQUARE_SIZE + SQUARE_SIZE * 0.8),
                    LINE_WIDTH
                )
            elif board.board[row][col] == 'O':
                pygame.draw.circle(
                    screen, O_COLOR,
                    (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                     row * SQUARE_SIZE + SQUARE_SIZE // 2),
                    SQUARE_SIZE // 3,
                    LINE_WIDTH
                )


def display_message(message):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    text = font.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    restart_text = font.render("Press 'R' to restart", True, TEXT_COLOR)
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_text, restart_rect)

    toggle_text = font.render(
        "Press 'T' to toggle AI algorithm", True, TEXT_COLOR)
    toggle_rect = toggle_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(toggle_text, toggle_rect)

    pygame.display.update()


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    board.reset()
    global player_turn
    player_turn = True  


def toggle_agent():
    global agent, use_alpha_beta
    use_alpha_beta = not use_alpha_beta
    agent = AlphaBetaAgent('O') if use_alpha_beta else MinimaxAgent('O')
    agent_type = "Alpha-Beta Pruning" if use_alpha_beta else "Regular Minimax"
    print(f"Switched to {agent_type} agent")
    return agent_type


draw_lines()

game_over = False
agent_type = "Alpha-Beta Pruning" if use_alpha_beta else "Regular Minimax"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and player_turn and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            row = mouseY // SQUARE_SIZE
            col = mouseX // SQUARE_SIZE

            if board.is_valid_move(row, col):
                board.make_move(row, col, 'X')
                player_turn = False

                if board.check_winner('X'):
                    print("Player wins!")
                    game_over = True
                    display_message("Player Wins!")
                elif board.is_full():
                    print("It's a tie!")
                    game_over = True
                    display_message("It's a Tie!")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
            elif event.key == pygame.K_t:
                agent_type = toggle_agent()
                if game_over:
                    restart()
                    game_over = False

    if not player_turn and not game_over:
        pygame.time.delay(300)

        start_time = time.time()

        row, col = agent.get_best_move(board)

        end_time = time.time()
        thinking_time = end_time - start_time
        print(f"{agent_type} AI move took {thinking_time:.6f} seconds")

        if board.is_valid_move(row, col):
            board.make_move(row, col, 'O')
            player_turn = True

            if board.check_winner('O'):
                print("AI wins!")
                game_over = True
                display_message("AI Wins!")
            elif board.is_full():
                print("It's a tie!")
                game_over = True
                display_message("It's a Tie!")

    if not game_over:
        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()

        ai_text = font.render(f"AI: {agent_type}", True, TEXT_COLOR)
        screen.blit(ai_text, (10, 10))

        pygame.display.update()
