from settings import *
from map import *
import pygame

st = open('./editor_settings.txt', 'r').readlines()



def render_map():
    for tx_line in text_map:
      for line in st:
        line = line.split()
        if tx_line[0] == line[0]:
          color = tuple(map(int, line[1].split(',')))
      if tx_line[0] == ' ':
        color = (255, 255, 255)    
      pygame.draw.rect(screen, color, tx_line[1], width=4)


def main():
    
    run = True

    while run:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))
        render_map()

        pygame.display.update()
                

def main_menu():
    main()



screen = pygame.display.set_mode((WIDTH, HEIGHT))

main_menu()
