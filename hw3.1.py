import random

class Human:
    def __init__(self, name='Human'):
        self.name = name
        self.money = 10
        self.gladness = 50
        self.satiety = 50
        self.job = None
        self.car = None
        self.home = None
        self.pet = None

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_pet(self):  # Використовуємо клас Pet замість Auto
        self.pet = Pet(pet_list)

    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
            else:
                self.satiety += 5
                self.home.food -= 5

    def work(self):
        if self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
            else:
                self.to_repair()

    def shopping(self, manage):
        if not self.car.drive():
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return

        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel = 100
        elif manage == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            self.gladness += 20
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 20
        self.home.mess += 5

    def play_with_pet(self):  # Звертаємось до self.pet
        self.gladness += self.pet.gladness_plus
        self.satiety -= self.pet.eat
        self.home.mess += self.pet.house_mess

    def clean_home(self):
        self.gladness -= 10
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def day_indexes(self, day):
        print(f'{f"Today the {day} of {self.name} life":=^50}')
        print(f'Money: {self.money}')
        print(f'Gladness: {self.gladness}')
        print(f'Satiety: {self.satiety}')
        print(f'{self.car.brand} car -> Fuel: {self.car.fuel}, Strength: {self.car.strength}')
        print(f'Home -> Food: {self.home.food}, Mess: {self.home.mess}')
        if self.pet:
            print(f'Pet: {self.pet.kind}')

    def is_alive(self):
        if self.satiety <= 0:
            print('Dead of hunger')
            return False
        if self.gladness <= 0:
            print('Depression...')
            return False
        if self.money < 0:
            print('Bankrupt...')
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        self.day_indexes(day)

        dice = random.randint(1, 6)
        if dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.chill()
        elif dice == 4:
            self.clean_home()
        elif dice == 5:
            self.shopping('delicacies')
        elif dice == 6:
            self.play_with_pet()

        return True

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):  # Додала логіку методу
        if self.fuel >= self.consumption and self.strength > 0:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot drive!')
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Pet:
    def __init__(self, pet_list):
        self.kind = random.choice(list(pet_list))
        self.house_mess = pet_list[self.kind]['mess']
        self.gladness_plus = pet_list[self.kind]['gladness+']
        self.eat = pet_list[self.kind]['eat']

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

brands_of_car = {
    'КАМАЗ': {'fuel': 50, 'strength': 300, 'consumption': 2},
    'Богдан': {'fuel': 180, 'strength': 270, 'consumption': 5},
    'Lada': {'fuel': 2, 'strength': 40, 'consumption': 6},
    'Lambrgumbr': {'fuel': 40, 'strength': 80, 'consumption': 6},
    'Mercedes': {'fuel': 50, 'strength': 350, 'consumption': 20}
}

job_list = {
    'Farmer': {'salary': 30, 'gladness_less': 10},
    'Freelancer': {'salary': 35, 'gladness_less': 15},
    'Python Developer': {'salary': 50, 'gladness_less': 20},
    'Driver': {'salary': 32, 'gladness_less': 25},
    'Delivery man': {'salary': 40, 'gladness_less': 20}
}

pet_list = {
    'Cat': {'mess': 15, 'gladness+': 45, 'eat': 15},
    'Dog': {'mess': 25, 'gladness+': 50, 'eat': 25},
    'Aquarium': {'mess': 5, 'gladness+': 25, 'eat': 5},
    'Parrot': {'mess': 10, 'gladness+': 25, 'eat': 7}
}

# === Запуск симуляції ===
human = Human(name='John')
human.get_home()
human.get_car()
human.get_pet()
human.get_job()

for day in range(1, 8):
    if not human.live(day):
        break