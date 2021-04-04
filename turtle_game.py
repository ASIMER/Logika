from turtle import *


class Sprite(Turtle):
    def __init__(self, x, y, my_color, my_shape, my_speed=5):
        super().__init__()
        self.shape(my_shape)
        self.color(my_color)
        self.penup()
        self.goto(x, y)
        self.my_speed = my_speed
        self.speed(0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.my_speed)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.my_speed)

    def move_left(self):
        self.goto(self.xcor() - self.my_speed, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.my_speed, self.ycor())

    def is_collide(self, target):
        dist = self.distance(target)
        return dist < 30

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end)) #направление

    def make_step(self):
        self.forward(self.my_speed) #направление уже есть

        if self.distance(self.x_end, self.y_end) < self.my_speed: #если расстояние меньше полушага
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start) #меняем направление


player_spawn_point_x, player_spawn_point_y = 0, -100

player = Sprite(x=0, y=player_spawn_point_y,
                my_color='yellow',
                my_shape='circle')

enemy1 = Sprite(x=-150, y=100,
                my_color='red',
                my_shape='square')
enemy2 = Sprite(x=150, y=150,
                my_color='red',
                my_shape='square')
goal = Sprite(x=0, y=200,
              my_color='green',
              my_shape='triangle')

enemy1.set_move(-200, 0, 200, 0)

enemy2.set_move(200, 70, -200, 70)
goal.set_move(-200, 120, 200, 0)



# Привязка клавиш
# получаем объект - экран
scr = player.getscreen()

# привязываем движение вверх, к клавишам w и up
scr.onkey(player.move_up, "w")
scr.onkey(player.move_up, "up")
# привязываем движение вниз, к клавишам s и down
scr.onkey(player.move_down, "s")
scr.onkey(player.move_down, "down")
# привязываем движение влево, к клавишам a и left
scr.onkey(player.move_left, "a")
scr.onkey(player.move_left, "left")
# привязываем движение вправо, к клавишам d и right
scr.onkey(player.move_right, "d")
scr.onkey(player.move_right, "right")

# включаем отслеживание нажатия клавиш
scr.listen()

# счетчик - сколько раз мы попали в зеленую стрелочку
score = 0
while score != 3:
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        exit()
    elif player.is_collide(goal):
        score += 1
        print("Текущий счет:", score)
        player.goto(x=player_spawn_point_x, y=player_spawn_point_y)
        enemy1.my_speed += 8
        enemy2.my_speed += 5

    enemy1.make_step()
    enemy2.make_step()
    goal.make_step()