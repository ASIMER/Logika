class Hero:
    def __init__(self, name, health=100,
                 damage=1, armor=1,
                 weapon="Кулаки"):
        self.name = name # Имя персонажа
        self.health = health # Здоровье
        self.damage = damage # Урон
        self.armor = armor # Броня
        self.weapon = weapon # Оружие

    def info(self):
        print("Имя:", self.name)
        print("Здоровье:", self.health)
        print("Урон:", self.damage)
        print("Броня:", self.armor)
        print("Оружие:", self.weapon)
        print(" ")


    def attack(self, target):
        damage = self.damage
        if target.armor < self.damage:
            damage -= target.armor
        else:
            damage = 0

        target.health = target.health - damage


player = Hero(name="Игрок", health=100, armor=2, damage=10)
enemy = Hero(name="Разбойник", health=60, armor=1)
dragon = Hero(name="Дракон", health=200, damage=10, armor=5)

player.info() # информация про игрока
enemy.info() # информация про врага

player.attack(enemy) # игрок нападает на врага

player.info() # информация про игрока
enemy.info() # информация про врага
