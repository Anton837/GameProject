import pygame

class Button:
    def __init__(self, rect, color=(80, 80, 80), text=None, func=None):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.text = text
        self.func = func

    def call(self):
        if self.func != None:
            self.func()

    def render(self, win):
        ms_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(ms_pos):
            pygame.draw.rect(win, self.color, self.rect)
        else:
            pygame.draw.rect(win, (255, 255, 255), self.rect)
        
        if self.text != None:
            font = pygame.font.SysFont("comicsans", 10)
            win.blit(font.render(str(self.text), 1, (0, 0, 0)), (self.rect.x, self.rect.y))
        
