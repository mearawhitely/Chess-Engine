import pygame
import pygame_gui

# size of the window
window_width = 1000
window_height = 800

# colors for the board squares
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

# number of rows/columns for an 8x8 board
cells = 8
cell_size = 800 / cells

pygame.init()

# create size of GUI window and the title of it
screen = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption('wacky chess')

screen.fill(grey)

def draw_board():
    for row in range(cells):
        for col in range(cells):
            if (row+col) % 2 == 0:
                color = white
            else:
                color = black

            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
            pygame.display.flip()

draw_board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
