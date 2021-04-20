from fast_clicker_colors import *
import pygame
import time
pygame.init()

'''создаём окно программы'''


mw = pygame.display.set_mode((600, 500)) #окно программы (main window)
mw.fill(BACKGROUND)
clock = pygame.time.Clock()

'''класс прямоугольник'''

class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height) #прямоугольник
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness): #обводка существующего прямоугольника
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

'''класс надпись'''

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def set_image(self, path: str, size: tuple) -> None:
        """
        устанавливаем изображение, вместо текста

        :param path: str - путь к изображению
        :param size: tuple - размер изображения
        :return: None
        """
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, size)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

cards = []
num_cards = 4

x = 70

for i in range(num_cards):
    new_card = Label(x, 170, 110, 110, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_image("img/click_img_trasp.gif", (110, 110))
    cards.append(new_card)
    x += 130




start_time = time.time()
old_time = time.time()
 
time_text = Label(0,0,50,50,BACKGROUND)
time_text.set_text('Время:',40, DARK_BLUE)
time_text.draw(20, 20)
 
score_text = Label(380,0,50,50,BACKGROUND)
score_text.set_text('Счёт:',45, DARK_BLUE)
score_text.draw(20,20)
 
timer = Label(50,75,50,40,BACKGROUND)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0,0)
 
score = Label(430,75,50,40,BACKGROUND)
score.set_text('0', 40, DARK_BLUE)
score.draw(0,0)

wait = 0

from random import randint

while True:
    if wait == 0:
        #переносим надпись:
        wait = 20 #столько тиков надпись будет на одном месте
        # генерируем случ число, что бы выбрать прямоугольник
        click = randint(1, num_cards)
        # перебираем прямоугольники,
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if (i + 1) == click:
                cards[i].draw(0, 0)
            else:
                cards[i].fill()
    else:
        wait -= 1

    #на каждом тике проверяем клик:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # узнаем куда мы нажали
            x, y = event.pos
            for i in range(num_cards):
                #ищем, в какую карту попал клик
                if cards[i].collidepoint(x,y) and (i + 1) == click:
                    cards[i].color(GREEN)

                elif cards[i].collidepoint(x,y):
                    #иначе перекрашиваем в красный, минус очко
                    cards[i].color(RED)

                cards[i].fill()

    pygame.display.update()
    clock.tick(40)