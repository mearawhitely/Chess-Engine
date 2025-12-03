import pygame
import random
from cell import Cell
from pieces import *
from pieces import Pawn, Bishop, Rook, Knight, Queen, King
from game import Game

pygame.init()

# ----------------- SETTINGS -----------------
WINDOW_WIDTH, WINDOW_HEIGHT = 1250, 800
NUM_CELLS = 8
CELL_SIZE = 800 // NUM_CELLS
WHITE, BLACK, GREY = (255, 255, 255), (0, 0, 0), (128, 128, 128)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wacky Chess")
clock = pygame.time.Clock()

# ----------------- GAME STATE -----------------
cells = []
white_pieces = []
black_pieces = []
current_piece = None
turn = 'white'

game_over = False
winner_text = ""

# ----------------- BOARD -----------------
def draw_board_once():
    for row in range(NUM_CELLS):
        for col in range(NUM_CELLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            cells.append(Cell(row, col, color, rect, False, None))

def draw_board():
    for cell in cells:
        pygame.draw.rect(screen, cell.GetColor(), cell.GetRect())
        if cell.GetHighlight():
            pygame.draw.rect(screen, (0, 255, 0), cell.GetRect(), 4)

def add_piece(piece_obj, row, col, target_list):
    target_list.append(piece_obj)
    for c in cells:
        if c.row == row and c.col == col:
            c.SetOccupied(True)
            c.SetPiece(piece_obj)

def populate_board():
    for col in range(8):
        img = pygame.image.load('Chess-Engine/images/white_pawn.png').convert_alpha()
        rect = img.get_rect(topleft=(col*CELL_SIZE, 6*CELL_SIZE))
        add_piece(Pawn(6, col, WHITE, 'Chess-Engine/images/white_pawn.png', img, rect),
                  6, col, white_pieces)

        img = pygame.image.load('Chess-Engine/images/black_pawn.png').convert_alpha()
        rect = img.get_rect(topleft=(col*CELL_SIZE, 1*CELL_SIZE))
        add_piece(Pawn(1, col, BLACK, 'Chess-Engine/images/black_pawn.png', img, rect),
                  1, col, black_pieces)

    piece_positions = [
        (Rook, 7, 0, WHITE, 'Chess-Engine/images/white_rook.png'),
        (Rook, 7, 7, WHITE, 'Chess-Engine/images/white_rook.png'),
        (Rook, 0, 0, BLACK, 'Chess-Engine/images/black_rook.png'),
        (Rook, 0, 7, BLACK, 'Chess-Engine/images/black_rook.png'),

        (Knight, 7, 1, WHITE, 'Chess-Engine/images/white_knight.png'),
        (Knight, 7, 6, WHITE, 'Chess-Engine/images/white_knight.png'),
        (Knight, 0, 1, BLACK, 'Chess-Engine/images/black_knight.png'),
        (Knight, 0, 6, BLACK, 'Chess-Engine/images/black_knight.png'),

        (Bishop, 7, 2, WHITE, 'Chess-Engine/images/white_bishop.png'),
        (Bishop, 7, 5, WHITE, 'Chess-Engine/images/white_bishop.png'),
        (Bishop, 0, 2, BLACK, 'Chess-Engine/images/black_bishop.png'),
        (Bishop, 0, 5, BLACK, 'Chess-Engine/images/black_bishop.png'),

        (Queen, 7, 3, WHITE, 'Chess-Engine/images/white_queen.png'),
        (Queen, 0, 3, BLACK, 'Chess-Engine/images/black_queen.png'),

        (King, 7, 4, WHITE, 'Chess-Engine/images/white_king.png'),
        (King, 0, 4, BLACK, 'Chess-Engine/images/black_king.png')
    ]

    for cls, row, col, color, img_path in piece_positions:
        img = pygame.image.load(img_path).convert_alpha()
        rect = img.get_rect(topleft=(col * CELL_SIZE, row * CELL_SIZE))
        target_list = white_pieces if color == WHITE else black_pieces
        add_piece(cls(row, col, color, img_path, img, rect), row, col, target_list)

# ----------------- MOVE LOGIC -----------------
def bot_move():
    global black_pieces, white_pieces, cells, turn

    # --------------------------
    # Helper: check if a square is attacked by white
    # --------------------------
    def square_is_dangerous(row, col):
        for wp in white_pieces:
            moves = wp.get_moves(cells)
            for m in moves:
                if m.row == row and m.col == col:
                    return True
        return False

    # --------------------------
    # Collect all legal black moves, with scoring
    # --------------------------
    scored_moves = []   # (score, piece, target_cell)

    for piece in black_pieces:
        moves = piece.get_moves(cells)
        if not moves:
            continue

        piece_is_hanging = square_is_dangerous(piece.GetRow(), piece.GetCol())

        for cell in moves:
            score = 0

            # 1. Prefer captures
            if cell.GetOccupied() and cell.GetPiece().color == WHITE:
                captured = cell.GetPiece()
                score += captured.rank * 10      # big bonus for material gain

            # 2. Avoid moving into danger
            if square_is_dangerous(cell.row, cell.col):
                score -= piece.rank * 8          # leaving piece in danger

            # 3. Avoid moving a piece that is already threatened (unless capturing)
            if piece_is_hanging:
                if not (cell.GetOccupied() and cell.GetPiece().color == WHITE):
                    score -= piece.rank * 4

            scored_moves.append((score, piece, cell))

    if not scored_moves:
        return  # no legal moves (should be stalemate)

    # --------------------------
    # Choose the move with highest score
    # --------------------------
    scored_moves.sort(key=lambda x: x[0], reverse=True)
    best_score = scored_moves[0][0]

    # Collect all top-scoring moves (adds variation)
    best_moves = [m for m in scored_moves if m[0] == best_score]

    score, piece, target_cell = random.choice(best_moves)

    # --------------------------
    # Execute the chosen move
    # --------------------------
    old_row, old_col = piece.GetRow(), piece.GetCol()

    # Capture
    if target_cell.GetOccupied():
        target = target_cell.GetPiece()
        if target.color == WHITE:
            white_pieces.remove(target)

    # Update piece
    piece.SetRow(target_cell.row)
    piece.SetCol(target_cell.col)
    piece.rect.topleft = (target_cell.col * CELL_SIZE, target_cell.row * CELL_SIZE)

    # Update board cells
    for c in cells:
        if c.row == old_row and c.col == old_col:
            c.SetOccupied(False)
            c.SetPiece(None)

    target_cell.SetOccupied(True)
    target_cell.SetPiece(piece)

    # Turn back to white
    turn = 'white'

    check_king_death()

def check_king_death():
    global game_over, winner_text

    white_king_alive = any(p.type == "King" and p.color == WHITE for p in white_pieces)
    black_king_alive = any(p.type == "King" and p.color == BLACK for p in black_pieces)

    if not white_king_alive:
        winner_text = "Black Wins! (White king died)"
        game_over = True

    if not black_king_alive:
        winner_text = "White Wins! (Black king died)"
        game_over = True

def draw_game_over_screen():
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    font_large = pygame.font.SysFont('calibri', 80)
    font_small = pygame.font.SysFont('calibri', 40)

    t1 = font_large.render("GAME OVER", True, (255, 0, 0))
    t2 = font_small.render(winner_text, True, (255, 255, 255))
    t3 = font_small.render("Press R to Restart", True, (200, 200, 200))

    screen.blit(t1, (WINDOW_WIDTH//2 - t1.get_width()//2, 200))
    screen.blit(t2, (WINDOW_WIDTH//2 - t2.get_width()//2, 320))
    screen.blit(t3, (WINDOW_WIDTH//2 - t3.get_width()//2, 400))

def restart_game():
    global cells, white_pieces, black_pieces, current_piece, turn, score
    global game_over, winner_text

    cells = []
    white_pieces = []
    black_pieces = []
    current_piece = None
    turn = 'white'
    score = 0
    game_over = False
    winner_text = ""

    draw_board_once()
    populate_board()

def highlight_valid_moves(piece):
    for cell in cells:
        cell.SetHighlight(False)

    if piece is None:
        return

    moves = piece.get_moves(cells)
    for cell in moves:
        cell.SetHighlight(True)

def get_cell_at_pos(pos):
    for cell in cells:
        if cell.GetRect().collidepoint(pos):
            return cell
    return None

# ----------------- INPUT BOX -----------------
name = ''
score = 0
active = False
font = pygame.font.SysFont('calibri', 40)
text_box = pygame.Rect(920, 6, 300, 40)

# ----------------- INITIALIZE -----------------
draw_board_once()
populate_board()

# ----------------- MAIN LOOP -----------------
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Game(name, score).StoreGame()
            running = False

        # BLOCK INPUT IF GAME OVER (only allow restart)
        if game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                restart_game()
            continue

        # ----------------- MOUSE -----------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            active = text_box.collidepoint(mouse_pos)
            clicked_cell = get_cell_at_pos(mouse_pos)

            if clicked_cell is None:
                continue

            if current_piece is None:
                if clicked_cell.GetOccupied():
                    piece = clicked_cell.GetPiece()
                    if (turn == 'white' and piece.color == WHITE) or \
                       (turn == 'black' and piece.color == BLACK):
                        current_piece = piece
                        highlight_valid_moves(current_piece)

            else:
                if clicked_cell.GetHighlight():
                    old_row, old_col = current_piece.GetRow(), current_piece.GetCol()

                    if clicked_cell.GetOccupied():
                        target = clicked_cell.GetPiece()
                        if target.color == WHITE:
                            white_pieces.remove(target)
                        else:
                            black_pieces.remove(target)

                    current_piece.SetRow(clicked_cell.row)
                    current_piece.SetCol(clicked_cell.col)
                    current_piece.rect.topleft = (clicked_cell.col * CELL_SIZE,
                                                  clicked_cell.row * CELL_SIZE)

                    for c in cells:
                        if c.row == old_row and c.col == old_col:
                            c.SetOccupied(False)
                            c.SetPiece(None)

                    clicked_cell.SetOccupied(True)
                    clicked_cell.SetPiece(current_piece)

                    turn = 'black' if turn == 'white' else 'white'
                    check_king_death()

                current_piece = None
                for c in cells:
                    c.SetHighlight(False)

        # ----------------- KEYBOARD -----------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

            if active:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

    # ----------------- BOT MOVE -----------------
    if turn == 'black' and not game_over:
        bot_move()

    # ----------------- DRAW -----------------
    screen.fill(GREY)
    draw_board()
    for piece in white_pieces + black_pieces:
        screen.blit(piece.image, piece.rect)

    pygame.draw.rect(screen, WHITE if active else BLACK, text_box, 4)
    screen.blit(font.render(name, True, BLACK), (text_box.x + 5, text_box.y + 5))
    screen.blit(font.render("Name:", True, BLACK), (text_box.x - 110, text_box.y))

    if game_over:
        draw_game_over_screen()

    pygame.display.update()
    clock.tick(50)

pygame.quit()
