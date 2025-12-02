import pygame  # pygame package
from cell import Cell  # self-made cell class
from pieces import *  # all self-made classes for chess pieces

pygame.init()  # initialize pygame

# size of the window itself
window_width = 1250
window_height = 800

# color codes
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

num_cells = 8  # number of cells per row/column
cell_size = 800 / num_cells  # size of each cell given board size

# create size of GUI window and the title of it
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('wacky chess')
clock = pygame.time.Clock()

screen.fill(grey)  # fill in background (for side panel)

cells = []  # list of all cells on board to keep track of them
white_pieces = []  # list of all white pieces on board to keep track of them
black_pieces = []  # list of all black pieces on board to keep track of them


def draw_board():
    for row in range(num_cells):
        for col in range(num_cells):
            if (row+col) % 2 == 0:
                color = white
            else:
                color = black

            x = col * cell_size
            y = row * cell_size
            new_rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, color, new_rect)  # create rectangle

            pygame.display.flip()

            new_cell = Cell(row, col, color, new_rect)
            cells.append(new_cell)


def populate_board():
    # first, add the pawns
    for i in range(8):
        # white pawns
        white_pawn_image = pygame.image.load(
            'images\\white_pawn.png').convert_alpha()
        white_pawn_rect = white_pawn_image.get_rect()
        white_pawn_rect.topleft = (i * 100, 600)
        screen.blit(white_pawn_image, white_pawn_rect)
        white_pawn = Pawn(i, 6, white, 'images\\white_pawn.png',
                          white_pawn_image, white_pawn_rect)
        white_pieces.append(white_pawn)
        pygame.display.flip()
        # black pawns
        black_pawn_image = pygame.image.load(
            'images\\black_pawn.png').convert_alpha()
        black_pawn_rect = black_pawn_image.get_rect()
        black_pawn_rect.topleft = (i * 100, 100)
        screen.blit(black_pawn_image, black_pawn_rect)
        black_pawn = Pawn(i, 1, white, 'images\\black_pawn.png',
                          black_pawn_image, black_pawn_rect)
        black_pieces.append(black_pawn)
        pygame.display.flip()

    # then, add the rooks
    # rook in a1
    white_rook_image = pygame.image.load(
        'images\\white_rook.png').convert_alpha()
    white_rook_rect = white_rook_image.get_rect()
    white_rook_rect.topleft = (0, 700)
    screen.blit(white_rook_image, white_rook_rect)
    white_rook = Rook(0, 7, white, 'images\\white_rook.png',
                      white_rook_image, white_rook_rect)
    white_pieces.append(white_rook)
    # rook in h1
    white_rook_image = pygame.image.load(
        'images\\white_rook.png').convert_alpha()
    white_rook_rect = white_rook_image.get_rect()
    white_rook_rect.topleft = (700, 700)
    screen.blit(white_rook_image, white_rook_rect)
    white_rook = Rook(7, 7, white, 'images\\white_rook.png',
                      white_rook_image, white_rook_rect)
    white_pieces.append(white_rook)
    # rook in a8
    black_rook_image = pygame.image.load(
        'images\\black_rook.png').convert_alpha()
    black_rook_rect = black_rook_image.get_rect()
    black_rook_rect.topleft = (0, 0)
    screen.blit(black_rook_image, black_rook_rect)
    black_rook = Rook(0, 0, black, 'images\\black_rook.png',
                      black_rook_image, black_rook_rect)
    black_pieces.append(black_rook)
    # rook in h8
    black_rook_image = pygame.image.load(
        'images\\black_rook.png').convert_alpha()
    black_rook_rect = black_rook_image.get_rect()
    black_rook_rect.topleft = (700, 0)
    screen.blit(black_rook_image, black_rook_rect)
    black_rook = Rook(7, 0, black, 'images\\black_rook.png',
                      black_rook_image, black_rook_rect)
    black_pieces.append(black_rook)

    # then, add the knights
    # knight in b1
    white_knight_image = pygame.image.load(
        'images\\white_knight.png').convert_alpha()
    white_knight_rect = white_knight_image.get_rect()
    white_knight_rect.topleft = (100, 700)
    screen.blit(white_knight_image, white_knight_rect)
    white_knight = Knight(1, 7, white, 'images\\white_knight.png',
                          white_knight_image, white_knight_rect)
    white_pieces.append(white_knight)
    # knight in g1
    white_knight_image = pygame.image.load(
        'images\\white_knight.png').convert_alpha()
    white_knight_rect = white_knight_image.get_rect()
    white_knight_rect.topleft = (600, 700)
    screen.blit(white_knight_image, white_knight_rect)
    white_knight = Knight(6, 7, white, 'images\\white_knight.png',
                          white_knight_image, white_knight_rect)
    white_pieces.append(white_knight)
    # knight in b8
    black_knight_image = pygame.image.load(
        'images\\black_knight.png').convert_alpha()
    black_knight_rect = black_knight_image.get_rect()
    black_knight_rect.topleft = (100, 0)
    screen.blit(black_knight_image, black_knight_rect)
    black_knight = Knight(1, 0, black, 'images\\black_knight.png',
                          black_knight_image, black_knight_rect)
    black_pieces.append(black_knight)
    # knight in g8
    black_knight_image = pygame.image.load(
        'images\\black_knight.png').convert_alpha()
    black_knight_rect = black_knight_image.get_rect()
    black_knight_rect.topleft = (600, 0)
    screen.blit(black_knight_image, black_knight_rect)
    black_knight = Knight(6, 0, black, 'images\\black_knight.png',
                          black_knight_image, black_knight_rect)
    black_pieces.append(black_knight)

    # then, add the bishops
    # bishop in c1
    white_bishop_image = pygame.image.load(
        'images\\white_bishop.png').convert_alpha()
    white_bishop_rect = white_bishop_image.get_rect()
    white_bishop_rect.topleft = (200, 700)
    screen.blit(white_bishop_image, white_bishop_rect)
    white_bishop = Bishop(2, 7, white, 'images\\white_bishop.png',
                          white_bishop_image, white_bishop_rect)
    white_pieces.append(white_bishop)
    # bishop in f1
    white_bishop_image = pygame.image.load(
        'images\\white_bishop.png').convert_alpha()
    white_bishop_rect = white_bishop_image.get_rect()
    white_bishop_rect.topleft = (500, 700)
    screen.blit(white_bishop_image, white_bishop_rect)
    white_bishop = Bishop(5, 7, white, 'images\\white_bishop.png',
                          white_bishop_image, white_bishop_rect)
    white_pieces.append(white_bishop)
    # bishop in c8
    black_bishop_image = pygame.image.load(
        'images\\black_bishop.png').convert_alpha()
    black_bishop_rect = black_bishop_image.get_rect()
    black_bishop_rect.topleft = (200, 0)
    screen.blit(black_bishop_image, black_bishop_rect)
    black_bishop = Bishop(2, 0, black, 'images\\black_bishop.png',
                          black_bishop_image, black_bishop_rect)
    black_pieces.append(black_bishop)
    # bishop in f8
    black_bishop_image = pygame.image.load(
        'images\\black_bishop.png').convert_alpha()
    black_bishop_rect = black_bishop_image.get_rect()
    black_bishop_rect.topleft = (500, 0)
    screen.blit(black_bishop_image, black_bishop_rect)
    black_bishop = Bishop(5, 0, black, 'images\\black_bishop.png',
                          black_bishop_image, black_bishop_rect)
    black_pieces.append(black_bishop)

    # then, add the queens
    # white queen
    white_queen_image = pygame.image.load(
        'images\\white_queen.png').convert_alpha()
    white_queen_rect = white_queen_image.get_rect()
    white_queen_rect.topleft = (300, 700)
    screen.blit(white_queen_image, white_queen_rect)
    white_queen = Queen(3, 7, white, 'images\\white_queen.png',
                        white_queen_image, white_queen_rect)
    white_pieces.append(white_queen)
    # black queen
    black_queen_image = pygame.image.load(
        'images\\black_queen.png').convert_alpha()
    black_queen_rect = black_queen_image.get_rect()
    black_queen_rect.topleft = (300, 0)
    screen.blit(black_queen_image, black_queen_rect)
    black_queen = Queen(3, 0, black, 'images\\black_queen.png',
                        black_queen_image, black_queen_rect)
    black_pieces.append(black_queen)

    # then, add the kings
    # white king
    white_king_image = pygame.image.load(
        'images\\white_king.png').convert_alpha()
    white_king_rect = white_king_image.get_rect()
    white_king_rect.topleft = (400, 700)
    screen.blit(white_king_image, white_king_rect)
    white_king = King(4, 7, white, 'images\\white_king.png',
                      white_king_image, white_king_rect)
    white_pieces.append(white_king)
    # black king
    black_king_image = pygame.image.load(
        'images\\black_king.png').convert_alpha()
    black_king_rect = black_king_image.get_rect()
    black_king_rect.topleft = (400, 0)
    screen.blit(black_king_image, black_king_rect)
    black_king = King(4, 0, black, 'images\\black_king.png',
                      black_king_image, black_king_rect)
    black_pieces.append(black_king)


draw_board()
populate_board()


name = ''
font = pygame.font.SysFont('calibri', 40)
text_box = pygame.Rect(920, 6, 300, 40)
active = False
color = pygame.Color('black')


running = True
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == pygame.MOUSEBUTTONDOWN:
            if text_box.collidepoint(events.pos):
                active = True
            else:
                active = False
        if events.type == pygame.KEYDOWN:
            if active:
                if events.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += events.unicode

    if active:
        color = pygame.Color('white')
    else:
        color = pygame.Color('black')
    pygame.draw.rect(screen, color, text_box, 4)
    surf = font.render(name, True, 'black')
    screen.blit(surf, (text_box.x + 5, text_box.y + 5))
    # text_box.w = max(100, surf.get_width()+10)
    enter_name = font.render("Name: ", True, 'black')
    screen.blit(enter_name, (text_box.x - 110, text_box.y))
    pygame.display.update()
    clock.tick(50)
