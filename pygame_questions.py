import pygame
from random import randint
pygame.init()

#создание окна игры
back = (255, 255, 255) #цвет фона (background)
window = pygame.display.set_mode((500, 500)) #окно программы (main window)
window.fill(back)
clock = pygame.time.Clock()

class TextArea:
    def __init__(self, x, y, width=300, height=50, color=(200, 200, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        #цвет заливки - или переданный параметр, или общий цвет фона
        self.fill_color = color

    #установить текст
    def set_text(self, text, fsize=30, text_color=(0, 0, 0)):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)

    #отрисовка прямоугольника с текстом
    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


    # Создаю объект-прямоугольник для вопроса
question = TextArea(x=50, y=100, width=400, height=70)
question.set_text(text='Вопрос', fsize=90)
# Создаю объект-прямоугольник для ответа
answer = TextArea(x=50, y=240, width=400, height=70)
answer.set_text(text='Ответ', fsize=90)

question.draw()
answer.draw()
questions = [
        'Что изучаешь в Алгоритмике?',
        'На каком языке говорят во Франции?',
        'Что растёт на яблоне?'
        ]
answers = [
        'Python',
        'Французский',
        'Яблоки'
        ]

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.key == pygame.K_q:
            index = randint(0, len(questions)-1)
            question.set_text(questions[index], 40)
            question.draw()
        elif event.key == pygame.K_a:
            index = randint(0, len(answers)-1)
            answer.set_text(answers[index], 40)
            answer.draw()
    clock.tick(40)
