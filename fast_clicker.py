import pygame
from fast_clicker_colors import *
import time
pygame.init()

'''создаём окно программы'''
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
# заливаем окно цветом
mw.fill(BACKGROUND)
clock = pygame.time.Clock()


class Area:
    '''класс прямоугольник'''
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height) #прямоугольник
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        
    def outline(self, frame_color, thickness): #обводка существующего прямоугольника
        pygame.draw.rect(mw, frame_color, self.rect, thickness)    
 

 
class Label(Area):
    '''класс надпись'''
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


# сохраняем прямоугольники
cards = []
# количество прямоугольников
num_cards = 4
# координаты первого прямоугольника
x = 70
 
for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card)
    x = x + 100 

while True:
    for card in cards:
        card.draw(10, 30)

    pygame.display.update()
    clock.tick(40)