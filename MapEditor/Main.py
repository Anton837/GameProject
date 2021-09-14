
import pygame

WIDTH = 700
HEIGHT = 900
FPS = 30
TILE = 25

f = open('./map.py', 'w')
st = open('./editor_settings.txt', 'r').readlines()




def save():
    f.seek(0)
    f.write(f'text_map = {entitys}')
    
    f.truncate()
    


def main():
    global entitys

    run = True
    entitys = [[' ', (0 * TILE, 0 * TILE, TILE, TILE)]]
    block = 'W'
    color = (255, 255, 255)

    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                
                run = False
            if e.type == pygame.KEYDOWN:
                for line in st:
                    line = line.split()
                    if e.key == int(line[2]):
                        block = line[0]
                        break
                if e.key == pygame.K_s:
                    save()
            
            if e.type == pygame.MOUSEMOTION:
                ms_pos = pygame.mouse.get_pos()
                cur_pos = (ms_pos[0] // TILE, ms_pos[1] // TILE)
                
                brick = [block, (cur_pos[0] * TILE, cur_pos[1] * TILE, TILE, TILE)]
                for entity in entitys:
                    if entity[1][0] == brick[1][0] and entity[1][1] == brick[1][1]:
                        entitys.remove(entity)

                if not(brick[1][0] == WIDTH // 2 and brick[1][1] == HEIGHT // 2):
                    entitys.append(brick)
                    save()
                

        screen.fill((255, 255, 255))

        for entity in entitys:
            for line in st:
                line = line.split()
                if entity[0] == line[0]:
                    color = tuple(map(int, line[1].split(',')))
            if entity[0] == ' ':
                color = (255, 255, 255)    
            pygame.draw.rect(screen, color, entity[1], width=0)

        pygame.display.update()



def main_menu():
    global screen

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    main()

if __name__ == '__main__':
    main_menu()
