import pygame
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
global current_piece
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wacky Chess")
clock = pygame.time.Clock()

# ----------------- DATA -----------------
cells = []
white_pieces = []
black_pieces = []
current_piece = None
turn = 'white'

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
    # --------- PAWNS ---------
    for col in range(8):
        # White pawns (row 6)
        img = pygame.image.load('Chess-Engine/images/white_pawn.png').convert_alpha()
        rect = img.get_rect(topleft=(col*CELL_SIZE, 6*CELL_SIZE))
        add_piece(Pawn(6, col, WHITE, 'Chess-Engine/images/white_pawn.png', img, rect), 6, col, white_pieces)
        
        # Black pawns (row 1)
        img = pygame.image.load('Chess-Engine/images/black_pawn.png').convert_alpha()
        rect = img.get_rect(topleft=(col*CELL_SIZE, 1*CELL_SIZE))
        add_piece(Pawn(1, col, BLACK, 'Chess-Engine/images/black_pawn.png', img, rect), 1, col, black_pieces)

    # --------- OTHER PIECES ---------
    # Data: (Class, row, col, color, image_path)
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
        rect = img.get_rect(topleft=(col*CELL_SIZE, row*CELL_SIZE))
        target_list = white_pieces if color == WHITE else black_pieces
        add_piece(cls(row, col, color, img_path, img, rect), row, col, target_list)

# ----------------- MOVE LOGIC -----------------
def highlight_valid_moves(piece):
    """Highlight cells where the selected piece can legally move."""
    # First, clear all highlights
    for cell in cells:
        cell.SetHighlight(False)

    if piece is None:
        return

    # Get moves from the piece itself
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
text_box = pygame.Rect(920,6,300,40)

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

        # --------------- MOUSE ----------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            active = text_box.collidepoint(mouse_pos)
            clicked_cell = get_cell_at_pos(mouse_pos)
            if clicked_cell is None:
                continue

            # Selecting piece
            
            if current_piece is None:
                if clicked_cell.GetOccupied():
                    if (turn=='white' and clicked_cell.GetPiece().color==WHITE) or (turn=='black' and clicked_cell.GetPiece().color==BLACK):
                        current_piece = clicked_cell.GetPiece()
                        highlight_valid_moves(current_piece)
            else:
                # Move piece if cell is highlighted
                if clicked_cell.GetHighlight():
                    old_row, old_col = current_piece.GetRow(), current_piece.GetCol()
                    # Capture
                    if clicked_cell.GetOccupied():
                        target = clicked_cell.GetPiece()
                        if target.color==WHITE:
                            white_pieces.remove(target)
                        else:
                            black_pieces.remove(target)
                    # Update piece
                    current_piece.SetRow(clicked_cell.row)
                    current_piece.SetCol(clicked_cell.col)
                    current_piece.rect.topleft = (clicked_cell.col*CELL_SIZE, clicked_cell.row*CELL_SIZE)
                    # Update cells
                    for c in cells:
                        if c.row==old_row and c.col==old_col:
                            c.SetOccupied(False)
                            c.SetPiece(None)
                    clicked_cell.SetOccupied(True)
                    clicked_cell.SetPiece(current_piece)
                    # Switch turn
                    turn = 'black' if turn=='white' else 'white'
                current_piece = None
                for c in cells:
                    c.SetHighlight(False)

        # --------------- KEYBOARD ----------------
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            else:
                name += event.unicode

    # ----------------- DRAW -----------------
    screen.fill(GREY)
    draw_board()
    for piece in white_pieces + black_pieces:
        screen.blit(piece.image, piece.rect)
    pygame.draw.rect(screen, WHITE if active else BLACK, text_box, 4)
    screen.blit(font.render(name, True, BLACK), (text_box.x+5, text_box.y+5))
    screen.blit(font.render("Name:", True, BLACK), (text_box.x-110, text_box.y))

    pygame.display.update()
    clock.tick(50)

pygame.quit()
