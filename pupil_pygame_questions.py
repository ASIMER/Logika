import pygame
pygame.init()

back = (255, 255, 0)
window = pygame.display.set_mode((500, 500))
window.fill(back)
clock = pygame.time.Clock()

class TextArea:
    def __init__(self, x, y, width=300, height=50, color=(200,200,255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def set_text(self, text, fsize=30, text_color=(0, 0, 0)):
        self.text = text

        self.image = pygame.font.Font(None,fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

question = TextArea(x=120, y=100, width=290, height=70)
question.set_text(text='test', fsize=90)

answer = TextArea(x=120, y=240, width=90, height=70)
answer.set_text(text='test', fsize=90)

question.draw()
answer.draw()

while True:
    pygame.display.update()
    clock.tick(40)