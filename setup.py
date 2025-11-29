import pygame

pygame.init()
# size of the window
window_width = 1250
window_height = 800

# colors for the board squares
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

# number of rows/columns for an 8x8 board
num_cells = 8
cell_size = 800 / num_cells

# create size of GUI window and the title of it
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('wacky chess')
clock = pygame.time.Clock()

screen.fill(grey)

def draw_board():
    for row in range(num_cells):
        for col in range(num_cells):
            if (row+col) % 2 == 0:
                color = white
            else:
                color = black

            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
            
            pygame.display.flip()

draw_board()

name = ''
font = pygame.font.SysFont('calibri',40)
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
    pygame.draw.rect(screen,color, text_box,4)
    surf = font.render(name,True,'black')
    screen.blit(surf, (text_box.x +5 , text_box.y +5))
    #text_box.w = max(100, surf.get_width()+10)
    enter_name = font.render("Name: ",True, 'black')
    screen.blit(enter_name, (text_box.x - 110, text_box.y))
    pygame.display.update()
    clock.tick(50)
