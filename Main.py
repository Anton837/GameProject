import pygame

from Button import Button
from settings import *

board = [[[(255, 255, 255), (x * TILE, y * TILE, TILE, TILE)] for x in range(draw_width // TILE)] for y in range(draw_height // TILE)]

def draw_settings():
    pygame.draw.rect(screen, (40, 40, 40), (draw_width, 0, menu_width, HEIGHT))
    draw_buttons()

def init_buttons():
    global buttons
    btn_size = 30
    buttons = []
    x = draw_width
    y = 0
    row_size = 4
    start_sz = 0
    for cl in colors:
        if start_sz >= row_size:
            start_sz = 0
            x = draw_width
            y += 10 + btn_size
        buttons.append(Button((x, y, btn_size, btn_size), color=cl))
        x += 10 + btn_size
        start_sz += 1

def click_button(ms_pos, color):
    for btn in buttons:
        if btn.rect.collidepoint(ms_pos):
            btn.call()
            return btn.color
    return color

def draw_buttons():
    for btn in buttons:
        pygame.draw.rect(screen, btn.color, btn.rect)

def draw_board():
    screen.fill((255, 255, 255))
    for x in range(draw_width // TILE):
        for y in range(draw_height // TILE):
            pygame.draw.rect(screen, board[y][x][0], board[y][x][1])
    draw_settings()
    pygame.display.update()

def main():
    run = True
    painting = 1
    color = colors["red"]
    init_buttons()
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    run = False     
            #has drawing
            if e.type == pygame.MOUSEBUTTONDOWN:
                ms_pos = pygame.mouse.get_pos()
                if ms_pos[0] < draw_width:
                    painting = painting % 2 + 1
                else:
                    color = click_button(ms_pos, color)
            #draw pixel
            if painting-1:
                ms_pos = pygame.mouse.get_pos()
                cur_pos = (ms_pos[0] // TILE, ms_pos[1] // TILE)
                if cur_pos[0] < draw_width // TILE:
                    board[cur_pos[1]][cur_pos[0]][0] = color
        draw_board() 

def main_menu():
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    main()

if __name__ == '__main__':
    main_menu()
