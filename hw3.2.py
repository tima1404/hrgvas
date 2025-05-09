import random

class Cat:
    def __init__(self, name='Cat'):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.energy = 50
        self.ate_count = 0
        self.alive = True
        self.day = 0

    def to_eat(self):
        self.satiety += 25
        self.ate_count += 1
        self.energy -= 10
        print(f'{self.name} поїв.')

    def to_chill(self):
        self.energy -= 10
        self.gladness += 25
        self.satiety -= 10
        print(f'{self.name} відпочив.')

    def to_sleep(self):
        self.energy += 30
        self.gladness -= 5
        self.satiety -= 25
        print(f'{self.name} поспав.')

    def day_indexes(self):
        print(f'\n{" Day " + str(self.day) + " ":=^50}')
        print(f'{self.name:^50}')
        print(f'Gladness - {self.gladness}')
        print(f'Satiety  - {self.satiety}')
        print(f'Energy   - {self.energy}')
        print(f'Total times ate - {self.ate_count}')

    def is_alive(self):
        if self.gladness <= 0:
            print(f'{self.name} впав у депресію і більше не хоче жити...')
            self.alive = False
        elif self.satiety <= 0:
            print(f'{self.name} помер від голоду...')
            self.alive = False
        elif self.energy <= 0:
            print(f'{self.name} помер від виснаження...')
            self.alive = False

    def live(self):
        while self.alive:
            self.day += 1
            action = random.choice([self.to_eat, self.to_chill, self.to_sleep])
            action()
            self.day_indexes()
            self.is_alive()


my_cat = Cat('Мурчик')
my_cat.live()