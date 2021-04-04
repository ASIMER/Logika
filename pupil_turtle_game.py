from turtle import*


class Sprite(Turtle):
    def __init__(self,x,y,color,shape,speed):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.speed = speed

    def move_up(self):
        self.goto(self.xcor(),self.ycor() + self.speed)

    def move_down(self):
        self.goto(self.xcor(),self.ycor() - self.speed)

    def move_right(self):
        self.goto(self.xcor(),self.ycor() + self.speed)

    def move_up(self):
        self.left(self.xcor(),self.ycor() - self.speed)

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        return dist<30

s_width = 200
s_height = 180
player = Sprite(x=0, y=-100,speed=10, shape='circle', color ='orange')
ennemy1 = Sprite(x=-s_width, y=-100,speed=10, shape='square', color ='red')
ennemy2 = Sprite(x=s_width, y=-70,speed=10, shape='circle', color ='red')
goal = Sprite(x=0, y=120,speed=10, shape='turtle', color ='green')
total_score = 0
scr = player.getscreen()

scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_up, 'w')
scr.listen()
scr.onkey(player.move_up, 'Down')
scr.onkey(player.move_up, 's')
scr.listen()
scr.onkey(player.move_up, 'left')
scr.onkey(player.move_up, 'a')
scr.listen()
scr.onkey(player.move_up, 'Rigth')
scr.onkey(player.move_up, 'd')
